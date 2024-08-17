class Person:
    def __init__(self,name,email):
        self.__name=name
        self.__email=email

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name  

    def get_Email(self):
        return self.__email
    def set_Enail(self,email):
        self.__email=email

    

per=Person("Ajay","satyamkumar1412")
print(per.getname())
per.setname("Satyam")
print(per.getname())

