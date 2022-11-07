import boto3
import os
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="/home/ec2-user/environment/LUITGreenTeam/Finn.JPG",
    Bucket="week14testbucket3",
    Key="Finn.JPG"
)
#how to upload multiple files at once.
import os
import glob
cwd=os.getcwd()
cwd=cwd+"/upload/"

files=glob.glob(cwd+"/home/ec2-user/environment/LUITGreenTeam/*.JPG")
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="week14testbucket3",
    Key=file.split("/"))