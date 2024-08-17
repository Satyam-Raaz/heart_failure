l1=[1.2,3,4]
l2=[3,4,3,6]
l3=[]
print(l2)

n=len(l1)
m=len(l2)

for i in l1:
    for j in l2:
        if i in l2:
            l3.append(i)
            l2.remove(i)
            break
            

print(l3)        
