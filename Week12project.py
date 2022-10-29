#Create a list of AWS services
#Project Requirements:

#1. The list should be empty initially.
#2. Populate the list using append or insert.
#3. Print the list and the length of the list.
#4. Remove two specific services from the list by name or by index.
#5. Print the new list and the new length of the list.

#1
List = []
#2.  
List.append('EC2')
List.append('IAM')
List.append('VPC')
List.append('S3')
List.append('DynamoDB')
List.append('CloudFormation')
List.append('VPC')
#3
print('Top 7 AWS Services:', List)
List_length = str(len(List))
#4
del List [1:3]
print('Top 5 AWS Services:', List)
#5
List_length = str(len(List))
print('# of Available Services:', List_length)