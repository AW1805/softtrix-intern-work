# Goal: To create table in DynamoDB.
import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

response = dynamodb.create_table(
    TableName='DemoTable',
    KeySchema=[
        {
            'AttributeName': 'UserID',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserID',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Table created successfully!")
