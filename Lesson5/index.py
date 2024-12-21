# Global variable
greeting = "Hello"

# Function to demonstrate Local and Global variables
def greet(name):
    # Local variable
    message = f"{greeting}, {name}!"  # Uses the global 'greeting'
    print(message)

# Function to demonstrate Default Arguments
def add_numbers(a, b=5):
    # b has a default value of 5 if not provided
    result = a + b
    print(f"The result of adding {a} and {b} is {result}")

# Calling the functions
greet("Alice")  # Local and Global variables in use
add_numbers(10)  # Using default argument for b
add_numbers(10, 7)  # Overriding the default argument for b
