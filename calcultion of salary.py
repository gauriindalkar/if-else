salary=int(input("enter how mach salary of scohool employes"))
if salary<5000:
    print(salary,"securety gard salary")
elif salary<15000:
    print(salary,"liabrary teacher salary")
elif salary<30000:
    print(salary,"subject teacher salary")
elif salary<50000:
    print(salary,"principle salary")
else:
    print("invaild")