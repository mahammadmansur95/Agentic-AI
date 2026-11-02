num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))


#random module

import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

print(random.choice(list1))

random.shuffle(list1)

print(list1)

print(random.random())