import json
import boto3

def calculate_totals(products, discount_rate, tax_rate):
    subtotal = sum(product['productPrice'] * product['quantity'] for product in products)
    discount_amount = subtotal * (discount_rate / 100)
    subtotal_after_discount = subtotal - discount_amount
    tax_amount = subtotal_after_discount * (tax_rate / 100)
    total_amount = subtotal_after_discount + tax_amount
    return subtotal, subtotal_after_discount, total_amount

def send_receipt(email, receipt):
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:region:account-id:topic-name'  
    sns.publish(
        TopicArn=topic_arn,
        Message=receipt,
        Subject='Your Order Receipt',
    )

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

def receipt_handler(event, context):
    order_details = json.loads(event['body'])
    receipt = generate_receipt(order_details)
    send_receipt(order_details['customerEmail'], receipt)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Receipt sent successfully'}),
        'headers': {
            'Content-Type': 'application/json'
        },
    }
