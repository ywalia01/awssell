import json
import boto3
import bcrypt
from botocore.exceptions import ClientError

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    email = body.get('email')
    password = body.get('password').encode('utf-8')
    
    # Check if user already exists
    try:
        response = table.get_item(Key={'UserID': email})
        if 'Item' in response:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'User already exists'})
            }
        
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'DynamoDB error', 'message': str(e)})
        }

    # Hash password
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    # Insert new user
    try:
        table.put_item(Item={'UserID': email, 'PasswordHash': hashed_password})
        return {
            'statusCode': 200,
            'body': json.dumps({'success': 'User registered'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'DynamoDB error', 'message': str(e)})
        }