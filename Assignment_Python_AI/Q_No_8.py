n=int(input("enter number"))
i=0
a=0
b=1
while(i<n):
    sum=a+b
    print(sum)
    a=b
    b=sum
    i=i+1
