class Engines:
    def engineDetails(self):
        print("car engine  model is 1254")

class Tyres:
    def  tyreDetails(self):
        print("car tyre is apollo")

class Doors:
    def doorDeatils(self):
        print("car door is automatic")

class Car:
    def __init__(self):
        self.engine=Engines()
        self.tyres=Tyres()
        self.doors=Doors()

    def printDetails(self):
        self.engine.engineDetails()
        self.tyres.tyreDetails()
        self.doors.doorDeatils()

c=Car()
c.printDetails()                                   
