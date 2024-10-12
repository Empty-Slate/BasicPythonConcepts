# # Basic Syntax
#
# try:
#     # Code that may cause an exception
#     risky_operation()
# except SpecificExceptionType:
#     # code to handle the exception
#     handle_error()
# except AnotherExceptionType:
#     # Handle another exception type
#     handle_another_error()
# else:
#     # Code to run if no exception occurs
#     print("Operation was successful!")
# finally:
#     # Code that will always execute
#     print("Cleanup code here.")

# Example of Exception Handling:
def divide_numbers(num1, num2):
    try:
        result = num1 / num2 # This line may raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please provide numbers only!")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Testing the function
divide_numbers(10, 2)    # Output: The result is: 5.0
divide_numbers(10,0)     # Output: Cannot divide by zero!
divide_numbers(10, 'a')  # Output: Error: Please provide numbers only!










