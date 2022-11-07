import boto3

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="Finn.jpg",
    Bucket="Week14testbucket",
    Key="Finn.jpg")