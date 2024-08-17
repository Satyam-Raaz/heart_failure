class comparison:
    def __init__(self,num):
        self.num=num

    def __gt__(self,O):
        if self.num>O.num: return True
        else: return False

num1=comparison(10)
num2=comparison(7)
print(num1>num2)