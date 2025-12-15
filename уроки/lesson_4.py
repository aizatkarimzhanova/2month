class Car:
    car_total = 0

    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
        Car.car_total += 1
    
    def drive(self):
        print(f"Car: {self.model} speed:{self.speed}")

    @classmethod
    def test(cls):
        print("test", Car.car_total)

    @classmethod
    def get_count(cls):
        # нет доступа к атрибутам, методам объектов
        # нельзя взать self 
        print(f"{cls.car_total} cls")
        print(f"all {Car.car_total} cars")

#    @staticmethod
def  validate_speed(val):
    if val < 0:
        raise ValueError("Value muct be positive")
    return True

print(Car.car_total)
car_honda = Car(model = "honda", speed = 150)
print(Car.car_total)
car_subaru = Car(model = "subaru", speed = 100)
print(Car.car_total)

car_honda.drive()
car_honda.get_count()
Car.get_count()
Car.test()
