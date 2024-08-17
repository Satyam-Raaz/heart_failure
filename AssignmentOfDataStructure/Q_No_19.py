l1=[1,2,3,4]
l2=[3,4,5,6]
l3=[]
for i in l1:
    l3.append(i)


for i in l2:
    for j in l1:
        if i not in l1:
            l3.append(i)
            break

print(l3)            
