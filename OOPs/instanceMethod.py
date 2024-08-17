class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def findAge(self):
        return self.age

per =person("vishwa",99)
#print(person("saurav",19)) address print
print(per.findAge())        