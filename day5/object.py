# Define a class
class Dog:
    # Constructor
    def __init__(self, name, breed, age):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable
        self.age = age  # Instance variable
    
    # Method to display information
    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    # Method to simulate barking
    def bark(self):
        return f"{self.name} says Woof!"

# Create an object (instance) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever", 4)

# Access object methods and properties
print(my_dog.describe())  # Outputs: Buddy is a 4-year-old Golden Retriever.
print(my_dog.bark())      # Outputs: Buddy says Woof!
