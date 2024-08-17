list=[1,"true",3,4,5]
n=len(list)
i=0; j=n-1
while(i<j):
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
    i=i+1
    j=j-1

print(list)    