s="satyam"
t="kumar"
l=[]
n=len(s)
m=len(t)
i=0;j=0
while(i<n):
    l.append(s[i])
    i=i+1

while(j<m):
    l.append(t[j])
    j=j+1  


temp=""

for i in l:
    temp=temp+i

print(temp)  

