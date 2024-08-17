n=int(input("enter number"))
sum=0
j=2
while(j<=n):
    i=2
    m=j
    flag=True
    while(i<m):
        if(m%i==0):
           flag=False
           break
        i=i+1
    if flag==True: sum=sum+m
    j=j+1
print(sum)
