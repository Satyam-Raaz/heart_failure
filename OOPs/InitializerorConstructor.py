class person:
    #constructor/initializer for object
    def __init__(self,name,age):
        self.name=name
        self.age=age

per1=person("vishwa",99)
per2=person("saurav",97)

print(per1.name)
print(per2.name)


class Person:
    def __init__(Self,name,age):
        Self.name=name
        Self.age=age

    def __init__(Self,name):
        Self.name=name

per =Person("vishwa mohan")
print(per.name)

#per1=Person(vishwa,99) error show because object goint to last method , multilple init not allowed
#print(per.name)

class PErsion:
    def __init__(self, name,age=99,hobby="cricter"):
        self.name=name
        self.age=age
        self.hobby=hobby
per1=PErsion("vishwa")
per2=PErsion("vishwa",56)
per3=PErsion("vishwa",45,"cook")

print(per1.hobby)

print(per2.hobby)

print(per3.hobby)
        


