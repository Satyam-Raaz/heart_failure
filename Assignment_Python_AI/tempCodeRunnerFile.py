print(5)
for i in range(2,10):

    j=2
    count=0
    while j<=i:
        if i%2==0:
            count+=1
        j+=1    
    if count==1:
        print(i)        