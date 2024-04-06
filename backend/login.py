import json
import boto3
import bcrypt
import jwt
from botocore.exceptions import ClientError

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

SECRET_KEY = "YOUR_SECRET_KEY"  # Use a strong, unique key

def get_jwt_secret():
    secret_name = os.environ['JWT_SECRET_ARN']
    client = boto3.client('secretsmanager')
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    return get_secret_value_response['SecretString']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    email = body.get('email')
    password = body.get('password').encode('utf-8')
    
    # Retrieve user from DynamoDB
    try:
        response = table.get_item(Key={'UserID': email})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
        user = response['Item']

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'DynamoDB error', 'message': str(e)})
        }
    
    # Verify password
    if bcrypt.checkpw(password, user['PasswordHash'].encode('utf-8')):

        secretKey = get_jwt_secret()
        # Generate JWT token
        token = jwt.encode({'user_id': user['UserID']}, secretKey, algorithm='HS256')
        return {
            'statusCode': 200,
            'body': json.dumps({'token': token})
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Invalid credentials'})
        }
