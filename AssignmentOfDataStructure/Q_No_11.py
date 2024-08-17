l=[1,1,2,3,4,5,1,2,1]
maxcount=0
index=-1
for i in l:
    count=0
    for j in l:
        if l[j]==l[i]:
            count+=1 
            if count>len(l)/2:
                break   
    if  count>maxcount:
        maxcount=count
        index=l[i]
        if maxcount>len(l)/2:
            break

ans=[]
for i in l:
    if index!=l[i]:
        ans.append(l[i])


print(ans)


