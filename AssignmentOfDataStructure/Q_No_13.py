l=[1,2,2,3,4,5,5,6,7]
n=len(l)
d={}
i=0

while(i>n-1):
    if l[i] in d.keys(): i=i+1
    else :
        count =0
        j=i
        while(j<n):
            if l[i]==l[j]: 
                count=count+1
                j=j+1
            else: j=j+1
        s={l[i]:count}    
        d.update(s)
        i=i+1

print(d)

