t1=(1,2,3,4)
t2=(3,4,5,6)
new_tuple=()
for i in t1:
    if i in t2:
        new_tuple=new_tuple+(i,) 

print(new_tuple)        

