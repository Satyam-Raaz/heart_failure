class person:
    def __init__(self,name,car):
        self.__name=name
        self.__car=car

    #getter method 
    def getName(self):
        return salf.__name 

    def getCar(self):
        return self.__car

    #setter method 

    def setName(self):
        self.__name=name   

    def setCar(self):
        self.__car=car   

per=person("vishwa",99)

print(per.getName())  

per.setName("vishwa mohan")
print(per.getName())   