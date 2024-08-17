class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
         print("Animal is eating")

class Dog(Animal):
    def __init__(self, name,type):
        super().__init__(name)
        self.type=type

class cat(Animal):
    def __init__(self, name,type):
        super().__init__(name)
        self.type=type
    