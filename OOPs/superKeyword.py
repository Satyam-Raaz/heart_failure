class Parent:
    property=90
    def eat(self):
        print("parent eating")  

class Child(Parent):
    property=99
    def eat(self):
        print("child is eating")

    def display(self):
        print(self.property)
        print(super().property)

    def callEat(self):
        self.eat()
        super().eat()    

obj=Child()
obj.display()

obj.callEat()


