def filter_primeno(n):
    count=0
    j=2
    while j<=n:
        if n%j== 0:
            count+=1
        j+=1    
    if count==1:
        return True
    else:
        return False   

l=[2,5,6,8,11,15]
print(list(filter(filter_primeno,l)))
