names = ["mansur", "sabeen", "humera", "pavan"]

for idx,name in enumerate(names, 1):
    print("idx,", idx,"name :", name)

bills = [50,60,100]

for name, bill in zip(names, bills):
    print("name :", name, "bill :", bill)