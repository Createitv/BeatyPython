class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)

    def display(self):
        super().display()
        print("I am from the Car Class")

    def printCarDetails(self):
        super().printDetails()


obj1 = Car("Suzuki", "Grey", "2015", 4)  # creating a car object
obj1.display()  # calling the Car class method display()
obj1.printCarDetails()
