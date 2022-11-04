import random

number = random.randint(0,10)
thresh = 3

print(number)

if(number > thresh):
    print("big number")
    
elif(number < thresh):
    print("small number")
else: # elif(number == 6)
    print("number is ", str(thresh))
if(number > thresh + 2):
    print("really big number")