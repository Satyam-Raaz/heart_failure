d1={"A":23,"B":15,"c":56}
d2={"A":32,"B":51,"c":6}

d={}


for i in d1:
    print(i)
    print(d1[i])


for i in d1:
    sum=d1[i]+d2[i]
    s={i:sum}
    d.update(s)
print(d)
