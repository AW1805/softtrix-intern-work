# Amazon S3 Practice (AWS CLI)

After configuring AWS CLI, I practiced working with Amazon S3 using CLI commands.

### Create Bucket

aws s3api create-bucket \
--bucket my-cli-practice-bucket \
--region ap-south-1 \
--create-bucket-configuration LocationConstraint=ap-south-1

### List Buckets

aws s3 ls

This command lists all S3 buckets in the AWS account.

### Upload File

Uploaded a local file from the Downloads folder to the bucket.

aws s3 cp ~/Downloads/test.txt s3://my-cli-practice-bucket/

### Verify Upload

aws s3 ls s3://my-cli-practice-bucket

This confirmed that the file was successfully uploaded.

### Download File

aws s3 cp s3://my-cli-practice-bucket/test.txt ~/Downloads/

### Delete File

aws s3 rm s3://my-cli-practice-bucket/test.txt

### Delete Bucket

aws s3 rb s3://my-cli-practice-bucket

### Result

Successfully created an S3 bucket, uploaded and downloaded files, and deleted the resources using AWS CLI.
