# Example of Method Overriding (using default arguments)
class MathOperations:
    def add(self, a, b, c=0):        # Default argument for c
        return a + b + c

# Creating an instance of MathOperations
math_op = MathOperations()

# Calling the add method with different numbers of arguments
print(math_op.add(5, 10))                #Output: 15(5 + 10 + 0)
print(math_op.add(5, 10, 15))         #Output: 30(5 + 10 + 15)

#Overring
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):    # Overriding the sound method
        return "Bark"

class Cat(Animal):
    def sound(self):    # Overriding the sound method
        return "Meow"

# Creating instance of Dog and Cat
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow

