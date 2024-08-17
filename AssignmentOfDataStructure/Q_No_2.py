s=input("enter string")
n=len(s)
i=0
count=0
while(i<n):
    if(s[i]=='a'): count=count+1
    elif(s[i]=='e'): count=count+1
    elif(s[i]=='i'): count=count+1
    elif(s[i]=='o'): count=count+1
    elif(s[i]=='u'): count=count+1
    i=i+1

print(count)    
