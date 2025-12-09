
class Car:
    #инициализатор(конструктор)
    """def __init__(self):       const
        self.color = "red"
        self.model = "Matiz"""
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")
        
    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

car_honda = Car(color = "black", model = "Honda")
car_subaru = Car("blue", "Subaru")
print(car_honda)
print(car_honda.color, car_honda.model, car_honda.fined)
car_honda.color = "green"
print(car_honda.color, car_honda.model, car_honda.fined)
print(car_subaru)
print(car_subaru.color, car_subaru.model)
car_honda.year = 2020
print(car_honda.year)

car_subaru.drive_to("Bishkek")
car_honda.change_color("yellow")
car_subaru.change_color("skyblue")
