class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        """When you try to access displayID() from outside the class, 
        the following error is generated:'Employee' object has no attribute '__displayID()'
        """
        print("ID:", self.ID)

    def dis(self):
        return self.__displayID()


Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.dis()  # this will generate an error
