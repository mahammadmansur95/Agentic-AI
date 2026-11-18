ingrediants = ['water', "milk"]
ingrediants.append('sugar')
ingrediants.remove('water')

print(f"ingredinats", ingrediants)

list1 = ["i", 'love']
list2 = ['you']
list3=[1,2,3,4]
list1.extend(list2)

print(f"extend ", list1)

ingrediants.insert(2, 'mansur')

print("insert :",ingrediants)

last_item = ingrediants.pop()
ingrediants.reverse()
print("reverse", ingrediants)
ingrediants.sort()
print("sort", ingrediants)
print("max :" , max(list3))
print("min :" , min(list3))

# operators
print("full 3 list using + : ", list1 + list2 + list3)
print('* 3:', ['sabeen'] * 3 )