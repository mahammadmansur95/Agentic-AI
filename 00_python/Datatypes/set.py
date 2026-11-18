set1 = {"1", "2", "3"}
set2 = {'4', '5', '1'}

# all
final = set1 | set2
print("all set :", final)

#common
common = set1 & set2
print("common", common)

#removing
diff = set1 - set2
print("removing - :", diff)

#membership
print("is 1 in set1 :", "1" in set1)


