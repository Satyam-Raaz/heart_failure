class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance=self.__balance+amount

    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance=self.__balance-amount
            return True
        else:
            False

    def check_balance(self):
        return self.__balance     


acc=BankAccount(1000)
print(acc.check_balance())      
acc.deposit(2000)
print(acc.check_balance())
acc.withdraw(1500)
print(acc.check_balance())
        
