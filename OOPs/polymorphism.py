class Animal:
    def eat(self):
        print("animal is etaing")

class Dog(Animal):
    def eat(self):
        print("dog is eating")

class Cat(Animal):
    def eat(self):
        print("Cat is eating")

c=Cat()
d=Dog()
a=Animal()

c.eat()
d.eat()
a.eat()

