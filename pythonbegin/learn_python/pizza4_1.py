pizzas=['fish','chicken','dog','pig']
for pizza in pizzas:
    print(pizza+',I like pepperoni pizza.')
print("I really love pizza!")
friend_pizzas=pizzas[:]
pizzas.append("rabbit")
friend_pizzas.append('vagetable')
print("My favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)
food_stable=('A',"B",'C','D','E')
for food in food_stable:
    print(food)
food_stable=('A',"B",'C','rice','pizza')
for food in food_stable:
    print(food)
food_a='A';food_b='apple'
if food_a in food_stable:
    print('yeah')
if food_b in food_stable:
    print('yeah')
if food_b not in food_stable:
    print('yeah')