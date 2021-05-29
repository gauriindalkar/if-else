num=int(input("enter a number"))
a=num%10
print(a,"it is last digit number")
if a%7==0:
    print("it is divisible by 7")
else:
    print("it is not divisible by 7")