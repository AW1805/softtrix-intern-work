# Goal: To update items in table.
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('DemoTable')

response = table.update_item(
    Key={
        'UserID': '123'
    },
    UpdateExpression="SET Age = :age",
    ExpressionAttributeValues={
        ':age': 35
    },
    ReturnValues="UPDATED_NEW"
)

print("Item updated successfully")
print(response)
