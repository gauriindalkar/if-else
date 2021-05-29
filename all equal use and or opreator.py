num=int(input("enter number"))
num1=int(input("enter number"))
num2=int(input("enter number"))
if num>=num1 and num1>=num2 and num2>=num:
    print("all are equal")
elif num==num1 or num1==num2 or num2==num:
    print("any of three is equal")
else:
    print("invaild")