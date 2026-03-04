# IAM User Practice (AWS CLI)

After working with S3, I practiced basic IAM user management using AWS CLI.

### Create IAM User

aws iam create-user --user-name adx-dev

This command created a new IAM user.

### Output

{
    "User": {
        "Path": "/",
        "UserName": "adx-dev",
        "UserId": "AIDAXXXXXXXXXXXXX",
        "Arn": "arn:aws:iam::ACCOUNT-ID:user/adx-dev",
        "CreateDate": "2026-03-03T09:04:21+00:00"
    }
}

### Delete IAM User

aws iam delete-user --user-name adx-dev

This command removed the IAM user from the AWS account.

### Verify Deletion

aws iam get-user --user-name adx-dev

AWS returned an error confirming the user no longer exists:

An error occurred (NoSuchEntity) when calling the GetUser operation: The user with name adx-dev cannot be found.

### Result

Successfully created and deleted an IAM user using AWS CLI.
