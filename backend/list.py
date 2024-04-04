import json

def list_products(event, context):
    # Updated product list with productPrice
    products = [
        {
            "productId": "1",
            "productTitle": "Product 1",
            "productDescription": "Description of Product 1",
            "productPrice": 20.00, 
            "productImage": "https://s3.amazonaws.com/your-bucket/product1.jpg",
            "productRating": 4.5,
            "productSeller": "Seller 1"
        },
        # Add more products as needed
    ]

    return {
        'statusCode': 200,
        'body': json.dumps(products),
        'headers': {
            'Content-Type': 'application/json'
        },
    }




