num=int(input("enter first number"))
num1=int(input("enter second number"))
symbol=input("enter a symbol")
if symbol=="+":
    print(num+num1)
elif symbol=="-":
    print(num-num1)
elif symbol=="*":
    print(num*num1)
elif symbol=="/":
    print(num/num1)
elif symbol=="%":
    print(num%num1)
else:
    print("given opertor is invaild")