class person:
    country="India"

    def __init__(self,name,age):
        self.name=name
        self.age=age

per1=person("vishwa",99)

per2=person("vishwa mohan",89)

print(per1.name,per1.country)
print(per2.name,per2.country)

print(person.country)