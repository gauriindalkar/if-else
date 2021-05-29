water=int(input("enter a leval"))
if water<1:
    print("fill the water")
elif water>1 and water<10:
    print("don't fill water")
elif water>10:
    print("water is overflow")