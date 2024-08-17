s=input("enter string")
set={1}
n=len(s)
i=0
while(i<n):
    set.add(s[i])
    i=i+1

if(n+1==len(set)):print("true")
else: print("false")