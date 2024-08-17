s=input("enter string")
n=len(s)
i=0 ;j=0
ans=""
while(j<n):
    if(s[i]==s[j]): j=j+1
    else :
        l=j-i
        if(l==1): ans=ans+s[i]
        else:
         ans=ans+s[i]
         ans=ans+"l"

        i=j 
    
l=j-i
if(l==1): ans=ans+s[i]
else:
  ans=ans+s[i]
  ans=ans+"l"

print(ans)
