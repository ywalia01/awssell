import json

def lambda_handler(event, context):
    # Updated product list with productPrice
    products = [
        {
            "productId": 1,
            "productTitle": "Wireless Noise-Cancelling Headphones",
            "productDescription": "Experience crystal-clear sound and immersive audio with these premium noise-cancelling headphones. Lightweight and comfortable for all-day use.",
            "productPrice": 199.99,
            "productImage": "https://images.unsplash.com/photo-1629367494173-c78a56567877?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=927&amp;q=80",
            "productRating": 4.7,
            "productSeller": "TechGear"
        },
        {
            "productId": 2,
            "productTitle": "Smart Watch with Fitness Tracker",
            "productDescription": "Stay connected and track your fitness goals with this sleek and stylish smartwatch. Features include heart rate monitoring, GPS, and water resistance.",
            "productPrice": 149.99,
            "productImage": "https://m.media-amazon.com/images/I/71JU-bUt-sL.jpg",
            "productRating": 4.3,
            "productSeller": "GadgetHub"
        },
        {
            "productId": 3,
            "productTitle": "High-Performance Gaming Laptop",
            "productDescription": "Dominate the gaming world with this powerful and ultra-fast gaming laptop. Equipped with the latest hardware and a stunning display.",
            "productPrice": 1499.99,
            "productImage": "https://m.media-amazon.com/images/I/51Qu24My+CL._AC_UF894,1000_QL80_.jpg",
            "productRating": 4.8,
            "productSeller": "TechPro"
        },
        {
            "productId": 4,
            "productTitle": "Premium Leather Messenger Bag",
            "productDescription": "Carry your essentials in style with this durable and sophisticated leather messenger bag. Ideal for work, travel, or everyday use.",
            "productPrice": 89.99,
            "productImage": "https://m.media-amazon.com/images/I/81Fx57SA5OL._AC_UF894,1000_QL80_.jpg",
            "productRating": 4.5,
            "productSeller": "LeatherCraft"
        },
        {
            "productId": 5,
            "productTitle": "Robotic Vacuum Cleaner",
            "productDescription": "Say goodbye to manual vacuuming with this smart robotic vacuum cleaner. It automatically cleans your floors and carpets, saving you time and effort.",
            "productPrice": 299.99,
            "productImage": "https://m.media-amazon.com/images/I/61eRk8uocmS._AC_UF894,1000_QL80_.jpg",
            "productRating": 4.2,
            "productSeller": "SmartHome"
        },
        {
            "productId": 6,
            "productTitle": "Premium Yoga Mat",
            "productDescription": "Enhance your yoga practice with this non-slip, eco-friendly yoga mat. Provides excellent cushioning and grip for a comfortable workout.",
            "productPrice": 59.99,
            "productImage": "https://m.media-amazon.com/images/I/81oeN4YQGCL._AC_UF894,1000_QL80_.jpg",
            "productRating": 4.6,
            "productSeller": "FitnessPro"
        },
        {
            "productId": 7,
            "productTitle": "Professional DSLR Camera",
            "productDescription": "Capture stunning photos and videos with this high-performance DSLR camera. Features advanced autofocus, high-resolution sensor, and versatile lens options.",
            "productPrice": 1299.99,
            "productImage": "https://m.media-amazon.com/images/I/71ROh7X7gtL._AC_UF894,1000_QL80_.jpg",
            "productRating": 4.9,
            "productSeller": "CameraWorld"
        },
        {
            "productId": 8,
            "productTitle": "Ergonomic Office Chair",
            "productDescription": "Improve your posture and comfort while working with this ergonomically designed office chair. Adjustable features and breathable mesh back support.",
            "productPrice": 179.99,
            "productImage": "https://m.media-amazon.com/images/I/71wG3iqE4WL._AC_UF1000,1000_QL80_.jpg",
            "productRating": 4.4,
            "productSeller": "OfficeSupplies"
        }
    ]


    return {
        'statusCode': 200,
        'body': json.dumps(products),
        'headers': {
            'Content-Type': 'application/json'
        },
    }