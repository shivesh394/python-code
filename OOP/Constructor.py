class Employee:
    def __init__(self,name,age,salary,gender):  #act as the constructor
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employee_details(self):
        print("Name of employee   : ",self.name)
        print("Age of employee    : ",self.age)
        print("Salary of employee : ",self.salary)
        print("Gender of employee : ",self.gender)

e1=Employee("Shivesh", 21, 300000, "Male")
e1.employee_details()