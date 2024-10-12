# Public Access:
class Person:
    def __init__(self, name, age):
        self.name = name   # Public attribute
        self.age = age     # Public attribute

    def display_info(self):       #Public method
        print(f"Name: {self.name}, Age: {self.age}")

#Accessing public members
p = Person("Alice", 30)
print(p.name)       # Output: Alice
p.display_info()    # Output: Alice, Age:30

# # Protected Access:
# class Person:
#     def __init__(self, name, age):
#         self.name = name   # Protected attribute
#
#     def display_info(self):     # Protected method
#         print(f"Name: {self.name}")
#
# class Employee(Person):
#     def__init__(self, name, age, emp_id):
#         super().__init__(name, age)
#         self.emp_id = emp_id
#
#     def display_employee_info(self):
#          print(f"Employee Name: {self._name}, Employee ID: {self.emp_id}")
#
# # Accessing protected members within a subclass
# e = Employee("John", 28, 102)
# e.display_employee_info()           # Output: Employee Name: John, Employee ID: 102

# Protected Access
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age

    def _display_info(self):  # Protected method
        print(f"Name: {self._name}, Age: {self._age}")

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display_employee_info(self):
        self._display_info()  # Accessing protected method
        print(f"Employee ID: {self.emp_id}")

# Accessing protected members within a subclass
e = Employee("John", 28, 102)
e.display_employee_info()
# Output:
# Name: John, Age: 28
# Employee ID: 102
cvcx


