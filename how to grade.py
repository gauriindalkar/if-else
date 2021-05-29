sub1=int(input("enter 1 sub marks"))
sub2=int(input("enter 2 sub marks"))
sub3=int(input("enter 3 sub marks"))
sub4=int(input("enter 4 sub marks"))
sub5=int(input("enter 5 sub marks"))
percentage=(sub1+sub2+sub3+sub4+sub5)/500*100
if (percentage>=90):
    print("grade a")
elif (percentage>=80):
    print("grade b")
elif (percentage>=70):
    print("grade c")
elif (percentage>=60):
    print("grade d")
elif (percentage>=40):
    print("grade e")
else:
    print("grade f")