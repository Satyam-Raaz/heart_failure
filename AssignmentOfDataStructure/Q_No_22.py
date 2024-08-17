s1={1,2,3}
s2={2,3,4}

ans=[]
print(type(ans))
for i in s1:
    if i not in s2:
        ans.append(i)
for i in s2:
    if i not in s1:
        ans.append(i)


print(ans)       
