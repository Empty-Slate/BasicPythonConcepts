# Defining a Class
class Car:
    # Constructor to initialize the object
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable
        self.year  = year   # Instance variable
    # Method to display car details
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating an object  (instance) of the class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

# Accessing the object's method
car1.display_info()   #Output: Car: Toyota Corolla, Year: 2020
car2.display_info()   #Output: Car: Honda Civic, Year: 2021

# #Attributes(Instance Variable)
# self.brand, self.model, self.year # These are instance variable

# #Methods
# def display_info(self): # This is a method

# #Constructor
# def _init_(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

# Creating and Using Objects:
# Creating an Object
car = Car("Ford", "Mustang", 2022)

# Accessing object attributes
print(car.brand)          # Output: Ford

#Calling object method
car.display_info()        # Output: Car: Ford Mustang, Year: 2022