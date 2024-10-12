#Single Inheritance:
class Animal:
    def sound(self):
        print("Animal makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print("Dog barks.")

# Creating an instance of the Dog class
dog = Dog()
dog.sound()     #Output: Animal makes a sound
dog.speak()     #Output: Dog barks

# Multiple Inheritance:
# Parent class 1
class Canine:
    def bark(self):
        print("Canine barks")

# Parent class 2
class Pet:
    def friendly(self):
        print("Pet is friendly.")

# Child class (inherits from both Canine and Pet)
class Dog(Canine, Pet):
    pass

# Creating an instance of the Dog class
dog = Dog()
dog.bark()        #Output: Canine barks.
dog.friendly()    #Output: Pet is friendly.

#Multilevel Inheritance:
# Base class
class Animal:
    def sound(self):
        print("Animal makes a sound.")

# Derived class (inherits from Animal)
class Mammal(Animal):
    def type(self):
        print("This is a mammal.")

#Further derived class (inherits from Mammal)
class Dog(Mammal):
    def speak(self):
        print("Dog barks.")

# Creating an instance of the Dog class
dog = Dog()
dog.sound()     #Output: Animal makes a sound.
dog.type()      #Output: This is a mammal.
dog.speak()     #Output: Dog barks.

#Hierarchical Inheritance:
#Base class
class Animal:
    def sound(self):
        print("Animal makes a sound.")

# Derived class 1 (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print("Dog barks.")

#Derived class 2 (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print("Cat meows.")

# Creating objects for both derived classes
dog = Dog()
cat = Cat()

dog.sound()   # Output: Animal makes a sound.
dog.speak()   # Output: Dog barks.

cat.sound()   # Output: Animal makes a sound
cat.speak()   # Output: Cat meows.

# Hybrid Inheritance:
# Base class
class Animal:
    def sound(self):
        print("Animal makes a sound.")

# Derived class (inherits from Animal)
class Mammal(Animal):
    def type(self):
        print("This is a mammal.")

class Bird(Animal):
    def fly(self):
        print("Birds can fly.")

class Bat(Mammal, Bird):
    def speak(self):
        print("Bat makes a sound.")

# Creating an instance of the Bat class
bat = Bat()
bat.sound()      # Output: Animal makes a sound.
bat.type()       # Output: This is a mammal.
bat.fly()        # Output: Bird can fly.
bat.speak()      # Output: Bat makes a sound.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Calling the parent class's constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Calling the parent class method
        print(f"{self.name} barks.")

dog = Dog("Buddy", "Labrodor")
dog.speak()

# Output:
# Buddy makes a sound.
# Buddy barks.

# Creating an Interface in Python:

from abc import ABC, abstractmethod

# Define an abstract base class (interface)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass       # Abstract method with no implementation

    @abstractmethod
    def perimeters(self):
        pass       # Abstract method with no implementation

# Subclass implementation the interface
class Circle(Shape):
    def __init(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2   # Implementing the area method

    def perimeters(self):
        return 2 * 3.14 * self.radius     # Implementing the perimeter method

# Creating objects

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Rectangle Area: {rectangle.area()}")              # Output: Rectangle Area: 20
print(f"Rectangle Perimeter: {rectangle.perimeter()}")    # Output: Rectangle Perimeter: 18

print(f"Circle Area: {circle.area()}")                    # Output: Circle Area: 28.26
print(f"Circle Perimeter: {circle.perimeter()}")          # Output: Circle Perimeter: 18.84

