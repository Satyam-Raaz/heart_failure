list1=[1,3,5,7]
list2=[2,4,6,8]
list=[]
n=len(list1)
m=len(list2)
i=0; j=0; k=0
while(i<n and j<m):
    if(list1[i]<=list2[j]):
        #list.append(list1[i])
        list.insert(k,list1[i])
        i=i+1
        k=k+1
    else :
        #list.append(list2[j])
        list.insert(k,list2[j])
        k=k+1
        j=j+1

while(i!=n):
    #list.append(list1[i])
    list.insert(k,list[i])
    k=k+1
    i=i+1

while(j!=m):
    #list.append(list2[j])
    list.insert(k,list2[j])
    k=k+1
    j=j+1    

print(list)