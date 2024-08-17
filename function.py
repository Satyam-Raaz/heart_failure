def firstfunc():
    print("hello world")
firstfunc()

#sum of two numbers
def sum(a,b):
    return a+b
print(sum(5,7))

#global and local scope/variable
x=101  #global scope
def funct():
    x=102 #local scope
    print(x)
funct()
print(x)  

#default Argument
def greet(name,message="good mor"):
    print(name,message)
greet("vishwa","hello")
greet("vishwa",)

#keyword arguments
def greets(name,age,message):
    print(message,name,"your age is",age)
greets("vishwa",99,"hello")
greets(age=99,message="hello",name="vishwa")    

#positional Argments
def add(a,b):
    print("a ",a)
    print("b ", b)
    print(a+b)
add(5,6)
add(6,5)   

#variables number of passing arguments
def sums(*args):
    print(type(args))
    print(args)

    sum=0
    for num in args:
        sum+=num
    return sum    

print(sums(1,2,3,4,5))

def fn(*args,a,b):
    print(a)
    print(b)
    print(args)
    print(*args)
#fn(5,6,1,2,3,)    
fn(1,2,3,4,a=5,b=6)

def display(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key,value in kwargs.items():
        print(key,"->",value)
display (name="vihwa",age=99,city="patna")

def fun(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    print(*kwargs)

fun(5,6,7,8,9,name="vishea",age=99)   

#def fun1(**kwargs,a,b):
   # print(a)
    #print(b)
   # print(kwargs)

#fun1(nmae="vishwa",age=99,5,6) Error show


#Implicit conversion
def add1(a,b):
    return a+b
print(add1(5,7))
print(add1(5.5,7.7))


#Function Nesting
def outer():
    print("hello from outer")
    def inner():
        print("hello from inner")

    return inner

fn=outer()
fn()
outer()()

#Pass by value
num=5
def modify_num(num):
    num+=1
    print(num)

modify_num(num)
print("original num ", num)

#Pass By reference
my_list=[1,2,3]
def modifylist(li):
    li.append(5)
    print(li)

print("before calling function",my_list)
modifylist(my_list)
print("After calling function",my_list)


#Lambda function
func=lambda x:x+10
print(func(5))

add=lambda a,b:a+b
print(add(5,6))

def my_func():
    return lambda msg:print(msg)
my_func()("hello world")
