class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class ElectricCar(Vehicle):
    def start(self):
        super().start()

class Tesle(ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesle ready")

tesla = Tesle()
tesla.start()
print(f"{Tesle.mro()}")
    