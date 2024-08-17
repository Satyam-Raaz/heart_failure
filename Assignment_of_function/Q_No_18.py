l=[-1,2,3,-4,5]

def product_postive(l):
    product=1
    for i in l:
        if i>0:
            product=product*i      

    return product     


print(product_postive(l))