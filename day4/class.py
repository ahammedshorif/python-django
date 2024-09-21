
class Person:
    # Initialize the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to display information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    # Method to greet the person
    def greet(self):
        print(f"Hello, {self.name}!")

# Create an object of the Person class
person1 = Person("Ovi", 30)

# call the constructor
person1.display_info()
person1.greet()
