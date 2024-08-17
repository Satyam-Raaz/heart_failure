class A:
    def meth1(self):
        print("hello from A")
class B:
    def  meth2(self):
        print("hello from B")

class C(A,B):
    def meth(self):
        print("hello from the child")

c=C()
c.meth()
#c.meth1()
#c.meth2()

print(C.__mro__)


