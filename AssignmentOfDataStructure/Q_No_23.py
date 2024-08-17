t1=(1,2,3,4)
t2=(3,4,5,6)
new_tup=()
def intersection(t1,t2,new_tup):
    for i in t1:
        if i in t2:
           new_tup=new_tup+(i,)
    print(new_tup)       
intersection(t1,t2,new_tup)