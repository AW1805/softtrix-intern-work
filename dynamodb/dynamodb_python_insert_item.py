# Goal: To insert items in table.
import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

response = dynamodb.put_item(
    TableName='DemoTable',
    Item={
        'UserID': {'S': '123'},
        'Name': {'S': 'John Doe'},
        'Age': {'N': '30'}
    }
)

print("Item inserted successfully!")
