distance=float(input("enter the number"))
if distance>0 and distance<100:
    print("cost will be 5 rupeese")
elif distance>100 and distance<500:
    print("cost will be 8 rupeese")
elif distance>500 and distance<1000:
    print("cost will be 10 rupeese")
elif distance>1000:
    print("cost will be 12 rupeese")
else:
    print("invaild")