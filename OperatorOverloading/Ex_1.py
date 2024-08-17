class Num:
    def __init__(self,num):
        self.num=num

    def __add__(self,U):
        return self.num+U.num

num1=Num(5)
num2=Num(7)

res=num1+num2
print(res)