girls=int(input("enter number"))
if girls==12:
    print("room is occuapied")
elif girls<=12:
    print(12-girls,"beds are left")
else:
    print(girls-12,"girls shift other room")