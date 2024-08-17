s1={'a','b','c'}
s2={'c','d','e'}
s3={'a','b','c'}

for i in s2:
    for j in s1:
        if i not in s1:
            s3.add(i)
            break

print(s3)        