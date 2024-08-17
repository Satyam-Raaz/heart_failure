n=int(input("enter number"))

def gen_square(n):
    for i in range(1,n+1):
        yield i**2

gen=gen_square(n) 


for num  in gen:
    print(num)