t=(1,2,3,4,1,4,3,1,2)
d={}
print(type(d))

def occurence(t,d):
    for  i in t:
        count=0
        for j in t:
            if i==j:
                count+=1
        s={i:count}
        d.update(s)
    print(d)


occurence(t,d)    


    