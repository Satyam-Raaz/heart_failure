n=int(input("enter number"))

def gen_prime(n):
    for i in range(2,n+1):
         j=2
         count=0
         while j<=i:
            if i%j==0:
               count+=1
            j+=1    
         if count==1:
            yield i                  


gen=gen_prime(n)
for num in gen:
    print(num)