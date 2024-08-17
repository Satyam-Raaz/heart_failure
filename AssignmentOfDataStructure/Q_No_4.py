s=input("enter string")
t=input("enter string")
set1=[]
set2=[]
n=len(s)
m=len(t)
i=0
j=0
flag=True
if(n!=m):flag=False
else:
    while(i<n):
      set1.append(s[i])
      set2.append(t[i])
      i=i+1 
    set1.sort()
    set2.sort()  
    while(j<n):
       if(set1[j]!=set2[j]):
          flag=False
          break
       j=j+1

print(flag)       