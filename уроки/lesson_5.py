class Animal:
    def move(self):
        print("move")

class Swiming(Animal):
    def move(self):
        print("swim")

class Fly(Animal):
    def move(self):
        print("Fly")

class Duck(Swiming, Fly):
    def move(self):
        print("swim and fly")

duck = Duck()
duck.move()
# MRO = method resolution order
print(f"{Duck.mro()}")

