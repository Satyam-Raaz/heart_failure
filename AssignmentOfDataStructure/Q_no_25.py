t1=(1,2,3,4)
x=2;y=5
new_tup=()
def intersection(t1,x,y,new_tup):
    for i in t1:
        if i>=x and i<=y:
           new_tup=new_tup+(i,)
    print(new_tup)       
intersection(t1,x,y,new_tup)
