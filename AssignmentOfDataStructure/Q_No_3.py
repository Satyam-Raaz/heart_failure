s=input("enter string")
n=len(s)
i=0; j=n-1
count=0
flag=True
while(i<j):
    if(s[i]!=s[j]):
        flag=False
        break
    i=i+1
    j=j-1

print(flag)
   