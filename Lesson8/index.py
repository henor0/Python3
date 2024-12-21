def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

# Rectangle dimensions
length = 5
width = 6

# Calculating area and perimeter
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

# Output results
print(f"Area of rectangle (Procedural): {area}")
print(f"Perimeter of rectangle (Procedural): {perimeter}")


class Rectangle:
    def __init__(self, length, width):
        # Instance variables
        self.length = length
        self.width = width

    def calculate_area(self):
        # Calculate the area of the rectangle
        return self.length * self.width

    def calculate_perimeter(self):
        # Calculate the perimeter of the rectangle
        return 2 * (self.length + self.width)

    def display_info(self):
        # Display the dimensions and calculated area and perimeter
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        print(f"Rectangle with length {self.length} and width {self.width}:")
        print(f"  Area: {area}")
        print(f"  Perimeter: {perimeter}")


# Creating instances of Rectangle
rect1 = Rectangle(5, 6)
rect2 = Rectangle(7, 3)

# Displaying information about the rectangles
rect1.display_info()
rect2.display_info()


class Person:
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        # Display the name and age
        print(f"Name: {self.name}, Age: {self.age}")

# Creating instances of Person
person1 = Person(name="Arion", age=24)
person2 = Person(name="Fury", age=36)

# Displaying information
person1.display_info()
person2.display_info()


