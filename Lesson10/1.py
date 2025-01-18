from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def introduce(self):
        pass


class Student(Person):
    def __init__(self, name, age, favorite_player="Camavinga"):
        super().__init__(name, age)
        self._favorite_player = favorite_player

    @property
    def favorite_player(self):
        return self._favorite_player

    @favorite_player.setter
    def favorite_player(self, player):
        self._favorite_player = player

    # Implement the abstract method
    def introduce(self):
        return f"Hello, my name is {self._name}, I am {self._age} years old, and my favorite player is {self._favorite_player}."

try:

    student = Student("Alex", 20)


    print(student.introduce())


    student.favorite_player = "Mbappe"
    print(student.introduce())

except ValueError as e:
    print(e)


from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

# Usage:
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
my_book.print_info()

