chai = input("choose your cup size (small/medium/large): ").lower()

if chai == 'small':
    print("10 rupees")
elif chai == 'medium' :
    print("15 rupees")
elif chai == 'large':
    print("20 rupees")
else:
    print("Unknown cup size")