
class Car:
    
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

class Truct(Car):
    def drive_to(self, destination):
        print(f"Truct {self.model} driving to {destination}")

    def test(self):
        print(f"truct ")



truct_1 = Truct("blac", "Mers")
truct_1.drive_to("Bishkek")
truct_1.test()

bus_1 = Bus("blu", "Honda",6)
print(bus_1.number)

