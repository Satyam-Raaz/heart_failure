class Complexum:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,C):
        return self.x+C.x,self.y+C.y
    
c1=Complexum(2,5)
c2=Complexum(3,5)
print(c1+c2)