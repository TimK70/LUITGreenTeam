count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")    


for i in [1, 2, 3, 4, 5]:
    print(i)
else:
    print('For loop completed')

colors = ['red', 'pink', 'blue', 'orange', 'green']
for color in colors:
    if color == 'orange':
        print('Orange is in the list')
        break
else:
    print("Orange is not in the list")