import random

for i in range(0, 5):
    print(i)

number = random.randint(0,100)

thresh = 17

counter = 0

while (number != thresh):
    counter += 1
    number = random.randint(0,100)
    
    if(counter > 100):
        break

print("Number equals", number)
print("Thresh equals", thresh)
print("Reran this many times", counter)