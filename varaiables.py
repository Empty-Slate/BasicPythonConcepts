x = 10            #Integer
y = "Hello"       #String
z = 3.14          #Float
is_active = True  #Boolean

# Example of Valid and Invalid Variables

# Valid Variables
name = "John"
_age = 25
salary1 = 50000

# Invalid Variables
# 1age = 25         # Starts with a number
# my-name = "John"  # Contains a hyphen
# for = 20          # Uses a reserved keyword

# Changing the Value of a Variable
x = 10    # x is an integer
x = "Hi"  # Now x is a string

# Variable Scope
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)

print(global_var)  # Accessible
my_function()      # Local variable only accessible within the function

