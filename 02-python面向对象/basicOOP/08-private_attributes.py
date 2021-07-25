class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve._Employee__salary)  # 2500
print("Salary:", Steve.__salary)  # this will cause an error
