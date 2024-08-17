s=input(str("enter a string"))
revString=""
n=len(s)
j=n-1

while(j>=0):
    revString=revString+s[j]
    j=j-1
print(revString)