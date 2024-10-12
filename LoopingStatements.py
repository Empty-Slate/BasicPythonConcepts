# # For-Loop
# for items in sequence:
#     # code to execute for each item

# Iterating over a list
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)

# #While Loop
# while condition:
#     # Code to execute if condition is true

# Example of while loop
x = 0
while x < 5:
    print(x)
    x += 1

# # Nested Loop
# for outer_item in outer_sequence:
#     for inner_item in inner_sequence:
#         # Code to execute

# Example
matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    for element in row:
        print(element)

#Loop-Control-Statements
for num in [1,2,3,4,5]:
    if num == 3:
        break    #Exit the loop
    print(num)