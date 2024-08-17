l=[1,2,3,4,8
   ,1,5,6,4]
ans=[]
for i in l:
    count=0
    for j in l:
        if i in ans:
            break
        else:
            if i==j:
              count+=1
    if count>=1:
        ans.append(i)

print(ans)        
