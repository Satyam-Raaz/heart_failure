l=["cat","dog","rat","dog","bat","cat"]
d={}

for i in l:
    count=0
    for j in l:
        if i==j:
            count+=1
        s={i:count}
        d.update(s)
print(d)        
