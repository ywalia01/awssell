import json
import boto3
from datetime import datetime
import random
import os

# Access environment variables
# ddb_table_name = os.getenv('DDB_RECEIPTS_TABLE_NAME')
sns_topic_arn = os.getenv('SNS_TOPIC_ARN')

def get_jwt_secret():
    secret_name = os.environ['REC_TABLE_SECRET_ARN']
    region_name = 'us-east-1'
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    
    # Parse the JSON string to extract the table name
    secret = json.loads(get_secret_value_response['SecretString'])
    table_name = secret.get('TableName')  # Assuming the key for the table name is 'TableName'
    
    if not table_name:
        raise ValueError("Table name not found in secret")
    
    return table_name


def calculate_totals(products, discount_rate, tax_rate):
    # Convert discount_rate and tax_rate to floats if they're passed as strings
    discount_rate = float(discount_rate)
    tax_rate = float(tax_rate)
    
    subtotal = sum(product['productPrice'] * product['quantity'] for product in products)
    discount_amount = subtotal * (discount_rate / 100)
    subtotal_after_discount = subtotal - discount_amount
    tax_amount = subtotal_after_discount * (tax_rate / 100)
    total_amount = subtotal_after_discount + tax_amount
    return subtotal, subtotal_after_discount, total_amount

def generate_receipt_id():
    """Generate a unique receipt ID using the current timestamp and a random sequence."""
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    random_sequence = random.randint(1000, 9999)
    return f"{timestamp}-{random_sequence}"

def insert_receipt_to_dynamodb(customer_email, receipt):

    ddb_table_name = get_jwt_secret()

    try:
        dynamodb = boto3.client('dynamodb')
        table_name = ddb_table_name
        receipt_id = generate_receipt_id()  # Generate a unique ID for the receipt
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'userEmail': {'S': customer_email},  # Adjusted variable name to be consistent
                'receiptId': {'S': receipt_id},  # Use the generated receipt ID
                'receipt': {'S': receipt}  # The receipt content
            }
        )
    except Exception as e:
        error_message = f"Failed to insert receipt into DynamoDB for {customer_email}: {str(e)}"
        raise Exception(error_message)

def send_receipt(email, receipt):
    try:
        # Insert the receipt into DynamoDB first
        insert_receipt_to_dynamodb(email, receipt)
        
        sns = boto3.client('sns')
        # response = sns.create_topic(Name=f"CustomerReceipts")
        # topic_arn = response['TopicArn']
        topic_arn = sns_topic_arn
        
        sns.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
        )
        
        sns.publish(
            TopicArn=topic_arn,
            Message=receipt,
            Subject='Your Order Receipt',
        )
        # Optionally, delete the topic if it's not going to be reused
        # sns.delete_topic(TopicArn=topic_arn)
    except Exception as e:
        error_message = f"Failed to send receipt to {email}: {str(e)}"
        raise Exception(error_message)

def generate_receipt(order_details):
    subtotal, subtotal_after_discount, total_amount = calculate_totals(
        order_details['products'], order_details['discountRate'], order_details['taxPercentage'])
    receipt_lines = [
        f"Order Date: {order_details['orderPlacedDate']} {order_details['orderPlacedTime']}",
        f"Customer Email: {order_details['customerEmail']}",
        "Products:"
    ]
    for product in order_details['products']:
        product_total_price = product['productPrice'] * product['quantity']
        receipt_lines.append(f"- {product['productId']} - {product['productTitle']} - "
                             f"Quantity: {product['quantity']} - Price: ${product['productPrice']:.2f} - "
                             f"Total: ${product_total_price:.2f}")
    
    receipt_lines.append(f"Total price for all products: ${subtotal:.2f}")
    receipt_lines.append(f"Price after Discount: ${subtotal_after_discount:.2f}")
    receipt_lines.append(f"Price after taxes: ${total_amount:.2f}")
    
    return "\n".join(receipt_lines)

def lambda_handler(event, context):
    try:
        order_details = json.loads(event['body'])
        receipt = generate_receipt(order_details)
        send_receipt(order_details['customerEmail'], receipt)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Receipt sent successfully'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*', 
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET'
            },
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'errorDetail': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*', 
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET'
            },
        }
