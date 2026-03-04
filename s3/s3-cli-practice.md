# Amazon S3 Practice (AWS CLI)

After configuring AWS CLI, I practiced working with Amazon S3 using CLI commands.

### Create Bucket

aws s3api create-bucket \
--bucket adx-demo-bucket-18 \
--region ap-south-1 \
--create-bucket-configuration LocationConstraint=ap-south-1

### List Buckets

aws s3 ls

This command lists all S3 buckets in the AWS account.

### Upload File

aws s3 cp ~/Downloads/test.txt s3://adx-demo-bucket-18/

### Verify Upload

aws s3 ls s3://adx-demo-bucket-18

This confirmed that the file was successfully uploaded.

### Download File

aws s3 cp s3://adx-demo-bucket-18/test.txt ~/Downloads/

### Delete File

aws s3 rm s3://adx-demo-bucket-18/test.txt

### Delete Bucket

aws s3api delete-bucket \
  --bucket adx-demo-bucket-18 \
  --region ap-south-1

### Result

Successfully created an S3 bucket, uploaded and downloaded files, and deleted the resources using AWS CLI.
