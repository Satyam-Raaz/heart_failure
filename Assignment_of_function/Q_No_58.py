class Employee:
    total_emloyee=0
    def __init__(self,name):
        self.name=name
        Employee.total_emloyee+=1

    def get_Employee_count(self):
        return Employee.total_emloyee

emp1=Employee("ajay")
emp2=Employee("vijay")
emp2=Employee("uijay")
print(emp1.get_Employee_count())        