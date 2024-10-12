# def function_name(parameters):
#     # Code to execute
#     return value  # Optional

# Simple function that adds two numbers
def add_numbers(a, b):
    return a + b

# Call the function
result = add_numbers(5,3)
print(result)         # Output: 8

# Calling a function
add_numbers(2, 3)    # Output: 5

# Function with no parameters
def greet():
    print("Hello, World!")

greet()         #Output: Hello, World!

# Function with default parameters:
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!

# Function with Arbitrary Arguments
def add(*numbers):
    return sum(numbers)
print(add(1,2,3))       # Output : 6

def person_info(**info):
    print(info)

person_info(name = "Alice", age=30, city="New York")
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Return Statement:
def square(x):
    return x*x
result = square(4)
print(result)          # Output :16

# #Lambda Functions
# lambda arguments: expression

#Lambda Functions for adding two numbers
add = lambda x, y: x + y
print(add(3, 5))          # Output: 8

# Functions with No Parameters and No Return Value
def greet():
    print("Hello, World!")

greet()           # Output: Hello, World!

# Functions with Parameters and No Return Value
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")    # Output: Hello, Alice!

# Functions with No Parameters and a Return Value
def get_greeting():
    return "Hello, World!"

message = get_greeting()
greet_person("Alice")    # Output: Hello, Alice!

# Functions with Parameters and a Return Value
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)            # Output: 8

# Positioning Arguments
def multiply(a,b):
    return a*b

print(multiply(2, 3))    #Output: 6

# Default Arguments:
def greet(name= "Guest"):
    print (f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("John")   # Output: Hello, John!

# Arbitrary Arguments(*args)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3))

# Keyword Arguments(**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name= "Alice", age= 30, city= "New York")

#Output:
#name: Alice
#age: 30
#city: New York
