class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
         print("Animal is eating")

class Dog(Animal):
    def __init__(self, name,type):
        super().__init__(name)
        self.type=type

class Pet(Dog):
    def __init__(self, name, type,house):
        super().__init__(name, type)
        self.house=house
                