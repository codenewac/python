numbers=list(range(3,30,3))
for value in numbers:
    print(value)
numbers=list(range(1,11))
numbers_1=[]
for value in numbers:
    numbers_1.append(value**3)
for value in numbers_1:
    print(value)
print(numbers_1)
numbers_2=[value**2 for value in range(1,11)]
print(numbers_2)
print(numbers_2[-3:])
print(numbers_2.pop())
print(numbers_2)
print("The first three items in the list are:")
print(numbers_2[0:3])
print("Three items in the middle of the list are:")
print(numbers_2[3:6])
print("The last three items in the list are:")
print(numbers_2[6:9])