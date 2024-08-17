n=int(input("enter number"))
i=1
while(i<=n):
    j=1
    k=1
    l=1
    while(j<=n-i):
        print(" ",end=" ")
        j=j+1
    while(k<=i):
        print("*",end=" ")
        k=k+1
    while(l<=i-1):
          print("*",end=" ")
          l=l+1      
    i=i+1
    print()