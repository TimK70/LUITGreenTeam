motorcycles = []
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
del motorcycles[3]
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycel I owned was a {first_owned.title()}.")

print(motorcycles)
