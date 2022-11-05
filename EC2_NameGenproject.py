import random
import string
import sys

#define function to determine string length
def EC2_namesize(size=10, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

#user input to enter department desired.
department = input("Enter Department: Accounting, FinOps, Marketing: ")

#function to allow for user to input lower case as well, with re-try if unsuccessful.
for _ in department:
    if department == "Accounting" or department.lower() == "accounting" :
        print("Processing..")
        break
    elif department == "FinOps" or department.lower() == "finops" :
        print("Processing..")
        break
    elif department == "Marketing" or department.lower() == "marketing" :
        print("Processing..")
        break
    else:
        print("Error: This Name Generator is only for specific departments. Please enter appropriate department: ")
        department = input("Enter Department: Accounting, FinOps, Marketing: ")

number = int(input("Enter number of EC2 instances: "))

if number < 1:
    print("Please enter number greater than 0 ")
elif number > 0:
    print("")
    
print("Generated EC2 Instance Names: ")

for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = unique_name + "-" + EC2_namesize()
    print("EC2 Instance's names: ", EC2_unique_name)
    