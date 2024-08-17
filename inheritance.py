class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name+"animal is eating")

class Dog(Animal):
    def __init__(self,name,type):
        Animal.__init__(self,name)
        self.type=type  
    def getnameDog(self):
        print(self.name)

    def gettypedog(self):
        print(self.type)        

dog=Dog("Moti","Dubberman")
dog.eat()
dog.getnameDog()
dog.gettypedog()