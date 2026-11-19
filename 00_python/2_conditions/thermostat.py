device_status = 'active'
temp=38

if device_status == 'active':
    if temp > 35:
        print("High temp alert!")
    else:
        print("temp is normal")
else:
    print("Device is offline")