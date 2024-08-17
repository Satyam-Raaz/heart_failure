n=int(input("enter number"))

def gen_even(n):
    i=2
    while i<=n:
        yield i
        i+=2 
        
gen=gen_even(n)

for num in gen:
    print(num)
