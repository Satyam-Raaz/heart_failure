def cube_root(num):
    assert(num>=0), "pass a positive number"
    return num**(1/3)

#print(cube_root(8))
#print(cube_root(-8))
#print("last line")

try:
    val=cube_root(-5)
    print(val)
except:
    print("please provide positive number") 
print("last line")       


def operate(num):
    try:
        result=5/num
    except ZeroDivisionError:
        print("cannot divide a number by zero")

    else :
        print(result)       

operate(2)        
operate(0) 
operate(-2)