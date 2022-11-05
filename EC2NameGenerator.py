import random
import string
import sys

def string_generator(size=10, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Enter department: Accounting, FinOps, Marketing: ")

for _ in department:
    if department == "Accounting" or department.lower() == "accounting" :
        print("Processing... ")
        break
    elif department == "FinOps" or department.lower() == "finops" :
        print("Processing... ")
        break
    elif department == "Marketing" or department.lower() == "marketing" :
        print("Processing... ")
        break
    elif not department:
        EC2_name = str(input("Error: This name generator is only for specific departments. Please enter appropriate department. ")
        
EC2_name = int(input("Enter desired number of EC2 Instances: "))

if nameofEC2 < 1:
    print("Please enter a number greater than 0")
elif name of EC2 > 0:
    print("")

print("EC2 Instance Names Generated: ")

for _ in range(1, number + 1):
    unique_name = department
    unique_EC2_name = unique_name + "_" + string_generator()
    print("EC2 Instance Name: ", unique_EC2_name)