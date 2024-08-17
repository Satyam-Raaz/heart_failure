s1={1,2,3}
s2={3,4,5}
union=[]
intersection=[]
diff=[]
for i in s1:
    if i in s2:
       intersection.append(i)


for i in s1:
    union.append(i)
for i in s2:
    if i not in union:
        union.append(i)


for i in s1:
    if i not in s2:
        diff.append(i)

print(union)
print(intersection)
print(diff)                






