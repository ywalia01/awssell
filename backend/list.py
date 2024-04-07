from decimal import Decimal
import json
import boto3
import os

# products_table_name = os.getenv('DDB_PRODUCTS_TABLE_NAME')

def get_jwt_secret():
    secret_name = os.environ['PROD_TABLE_SECRET_ARN']
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

def check_and_insert_products(products):
    products_table_name = get_jwt_secret()
    print(f"Retrieved table name from Secrets Manager: {products_table_name}")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(products_table_name)
    
    try:
        # Check if any product is already present
        response = table.scan()
        if response['Items']:  # If there are already items in the table, no need to insert
            print("Products are already present. Skipping insertion.")
            return
        
        print("No products found. Inserting new products.")
        with table.batch_writer() as batch:
            for product in products:
                batch.put_item(Item=product)
                
    except Exception as e:
        error_message = f"Error during product check or insertion: {str(e)}"
        print(error_message)
        raise Exception(error_message)

def retrieve_products():
    products_table_name = get_jwt_secret()
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(products_table_name)
    
    try:
        response = table.scan()
        items = response.get('Items', [])
        return items
    except Exception as e:
        error_message = f"Failed to retrieve products from DynamoDB: {str(e)}"
        print(error_message)
        raise Exception(error_message)

def convert_decimals(obj):
    if isinstance(obj, list):
        return [convert_decimals(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_decimals(value) for key, value in obj.items()}
    elif isinstance(obj, Decimal):
        # Convert Decimals. Use str(value) for string representation or float(value) if that's acceptable
        return float(obj)
    else:
        return obj

def lambda_handler(event, context):
    # Updated product list with productPrice
    products = [
        {
            "productId": 1,
            "productTitle": "Wireless Noise-Cancelling Headphones",
            "productDescription": "Experience crystal-clear sound and immersive audio with these premium noise-cancelling headphones. Lightweight and comfortable for all-day use.",
            "productPrice": 199,
            "productImage": "https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=927&amp;q=80",
            "productRating": 5,
            "productSeller": "TechGear"
        },
        {
            "productId": 2,
            "productTitle": "Smart Watch with Fitness Tracker",
            "productDescription": "Stay connected and track your fitness goals with this sleek and stylish smartwatch. Features include heart rate monitoring, GPS, and water resistance.",
            "productPrice": 149,
            "productImage": "https://m.media-amazon.com/images/I/71JU-bUt-sL.jpg",
            "productRating": 4,
            "productSeller": "GadgetHub"
        },
        {
            "productId": 3,
            "productTitle": "High-Performance Gaming Laptop",
            "productDescription": "Dominate the gaming world with this powerful and ultra-fast gaming laptop. Equipped with the latest hardware and a stunning display.",
            "productPrice": 1499,
            "productImage": "https://m.media-amazon.com/images/I/51Qu24My+CL._AC_UF894,1000_QL80_.jpg",
            "productRating": 4,
            "productSeller": "TechPro"
        },
        {
            "productId": 4,
            "productTitle": "Premium Leather Messenger Bag",
            "productDescription": "Carry your essentials in style with this durable and sophisticated leather messenger bag. Ideal for work, travel, or everyday use.",
            "productPrice": 89,
            "productImage": "https://m.media-amazon.com/images/I/81Fx57SA5OL._AC_UF894,1000_QL80_.jpg",
            "productRating": 3,
            "productSeller": "LeatherCraft"
        },
        {
            "productId": 5,
            "productTitle": "Robotic Vacuum Cleaner",
            "productDescription": "Say goodbye to manual vacuuming with this smart robotic vacuum cleaner. It automatically cleans your floors and carpets, saving you time and effort.",
            "productPrice": 299,
            "productImage": "https://m.media-amazon.com/images/I/61eRk8uocmS._AC_UF894,1000_QL80_.jpg",
            "productRating": 2,
            "productSeller": "SmartHome"
        },
        {
            "productId": 6,
            "productTitle": "Premium Yoga Mat",
            "productDescription": "Enhance your yoga practice with this non-slip, eco-friendly yoga mat. Provides excellent cushioning and grip for a comfortable workout.",
            "productPrice": 59,
            "productImage": "https://m.media-amazon.com/images/I/81oeN4YQGCL._AC_UF894,1000_QL80_.jpg",
            "productRating": 4,
            "productSeller": "FitnessPro"
        },
        {
            "productId": 7,
            "productTitle": "Professional DSLR Camera",
            "productDescription": "Capture stunning photos and videos with this high-performance DSLR camera. Features advanced autofocus, high-resolution sensor, and versatile lens options.",
            "productPrice": 1299,
            "productImage": "https://m.media-amazon.com/images/I/71ROh7X7gtL._AC_UF894,1000_QL80_.jpg",
            "productRating": 3,
            "productSeller": "CameraWorld"
        },
        {
            "productId": 8,
            "productTitle": "Ergonomic Office Chair",
            "productDescription": "Improve your posture and comfort while working with this ergonomically designed office chair. Adjustable features and breathable mesh back support.",
            "productPrice": 179,
            "productImage": "https://m.media-amazon.com/images/I/71wG3iqE4WL._AC_UF1000,1000_QL80_.jpg",
            "productRating": 4,
            "productSeller": "OfficeSupplies"
        }
    ]
    
    # for product in products:
    #     product['productPrice'] = Decimal(str(product['productPrice']))

    # Check if products exist and insert if they don't
    check_and_insert_products(products)
    
    # Always retrieve and return products
    try:
        all_products = retrieve_products()
        all_products = convert_decimals(all_products)  # Convert Decimal types before serialization
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Products retrieval successful.', 'products': all_products}),
            'headers': {
                'Content-Type': 'application/json'
            },
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to retrieve products', 'errorDetail': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            },
        }