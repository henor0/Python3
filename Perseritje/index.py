class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

    def __str__(self):
        return f"Student Name: {self.__name}, Student Age: {self.__age}"

student = Student("Alice", 20)

print(student)

student.set_name("Bob")
student.set_age(25)

print(student)