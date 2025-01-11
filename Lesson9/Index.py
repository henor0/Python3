class Animal:
    def sound(self):
        print("Some animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("woof woof")

class Cat(Animal):
    def sound(self):
        print("meow meow")


animal_instance = Animal()
dog_instance = Dog()
cat_instance = Cat()

animal_instance.sound()
dog_instance.sound()
cat_instance.sound()


# Base class: Vehicle
class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")

    def drive(self):
        raise NotImplementedError("Subclass must implement this method")


# Derived class: Car
class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"{self.model} car engine started")

    def drive(self):
        print(f"{self.model} car is driving")


# Derived class: Truck (Another type of vehicle)
class Truck(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"{self.model} truck engine started")

    def drive(self):
        print(f"{self.model} truck is hauling cargo")


# Derived class: Motorcycle (Another type of vehicle)
class Motorcycle(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"{self.model} motorcycle engine started")

    def drive(self):
        print(f"{self.model} motorcycle is speeding")


# Function to demonstrate polymorphism
def start_and_drive(vehicle: Vehicle):
    vehicle.start_


strangth_langth = "Hello World"
Lengs_langth = [1, 2, 3, 4, 5, 6, 7, 8]
tooples_lengths = ()

# Corrected access to lengths
print(len(strangth_langth))  # Length of string
print(len(Lengs_langth))      # Length of list
print(len(tooples_lengths))   # Length of tuple
