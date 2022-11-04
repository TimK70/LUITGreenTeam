import random
import string
import sys

def string_generator (size =10, string=string.digits + string.ascii_letters):
    return "".join(random.choice(string) for _ in range(size))
    
department = input("Enter Department: Accounting, FinOps, Marketing: ")

for _ in department:
    if department == "Accounting" or department.lower() == 'accounting' :
        print("Processing... ")
        break
    elif department == "FinOps" or department.lower() == 'finops' :
        print("Processing... ")
        break
    elif department == "Marketing" or department.lower() == "marketing" :
        print("Processing... ")
        break
    else:
        print("Error: This Name Generator is only for specific departments. Please enter appropriate department. ")
        raise SystemExit

number = int(input("Enter desired number of EC2 Instances: "))

if number < 1:
    print("Please enter a number greater than 0. ")
elif number > 0:
    print("")
    
print("EC2 Instance Names Generated: ")

for _ in range(1, number + 1):
    unique_name = department
    unique_EC2_name = unique_name + "_" + string_generator()
    print("EC2 Instance Name: ", unique_EC2_name)