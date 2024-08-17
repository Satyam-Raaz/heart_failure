a=int(input("enter first number"))

b=int(input("enter second number"))
c=int(input("enter third number"))

max_num=lambda a,b,c: max(a,b,c)
print(max_num(a,b,c))