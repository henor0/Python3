class Pet:
    def __init__(self, name, age, species, breed, color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color

    def make_sound(self):
        print(f"{self.name} makes a sound!")

    def sleep(self):
        print(f"{self.name} is sleeping...")

    def eat(self):
        print(f"{self.name} is eating...")

# Example usage:
my_pet = Pet(name="Buddy", age=3, species="Dog", breed="Golden Retriever", color="Golden")

print(f"My pet's name is {my_pet.name}.")
my_pet.make_sound()
my_pet.sleep()
my_pet.eat()
