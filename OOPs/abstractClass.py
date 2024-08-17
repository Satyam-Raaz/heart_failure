from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

#a=Animal()    

class Dog(Animal):
    def sleep(self):
        print("Dog is sleeping")

    def eat(self):
        print("Dog is sleeping")

d=Dog()            