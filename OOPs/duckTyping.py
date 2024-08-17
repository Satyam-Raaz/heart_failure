class BirdFly:
    def flyBird(self,bird):
        bird.fly()

class Parrot:
    def fly(self):
        print("parrot is eating")

class Crow:
    def fly(self):
        print("crow is eating")

p=Parrot()
c=Crow()

p.fly()
c.fly()

bf=BirdFly()
bf.flyBird(p)
bf.flyBird(c)