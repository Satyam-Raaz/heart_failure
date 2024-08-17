d={"A":23,"B":15,"c":56}

for i in d:
    for j in d:
       if d[i]>d[j]:
           temp=i
           i=j
           j=temp

print(d)           