class Vehicle:  # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):  # child class of Vehicle
    def openTrunk(self):
        print("Trunk is now open.")


class Hybrid(Car):  # child class of Car
    def turnOnHybrid(self):
        print("Hybrid mode is now switched on.")


priusPrime = Hybrid()  # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class
