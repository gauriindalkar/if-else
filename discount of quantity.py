quantity=int(input("enter quantity"))
if quantity*100>1000:
    print("cost of",(quantity*100)-(quantity*100//10))
else:
    print("cost of",(quantity*100))