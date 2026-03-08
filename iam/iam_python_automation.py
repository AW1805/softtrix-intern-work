import boto3

iam = boto3.client("iam")

user_name = "python-demo-user"

iam.create_user(UserName=user_name)
print("User created:", user_name)

iam.delete_user(UserName=user_name)
print("User deleted:", user_name)
