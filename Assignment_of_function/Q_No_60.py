class Circle:
    def ___init__(self,radius):
        self.radius=radius

    @classmethod
    def calculate_area(cls):
        radius=cls.radius
        return cls(3.14*radius*radius)
    
    
cal=Circle(1)    
print(cal.calculate_area())    