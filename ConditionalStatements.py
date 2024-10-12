# # if statement
# if condition:
#     # Code to execute if condition is True

x = 10
if x > 5:
    print("X is greater than 5")

# # if-else statement
# if condition:
#     # Code to execute if condition is true
# else:
#     # Code to execute if condition is false

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# # if-else-if statement
# if condition1:
#     # Code to execute if condition1 is true
# elif condition2:
#     # Code to execute if condition2 is true
# else:
#     # Code to execute if none of the condition is true

x = 7
if x > 10:
    print("x ix greater than 10")
elif x == 7:
    print("x is equal to 7")
else:
    print("x is less than 10 and not equal to 7")


# # Nested-if-statement
# if condition1:
#     if condition2:
#         # Code to execute if both condition1 and condition2 are false

x = 8
if x > 5:
    if x <10:
        print("x is between 5 and 10")

# # Conditional-Expressions(Ternary-Operator)
# result = value_if_true if conditional else value_if_false

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)     # Output: Even