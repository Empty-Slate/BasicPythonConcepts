# list in Python (acting as an array)
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])

# Modifying elements
numbers[1] = 10

# Adding elements
numbers.append(5)

# Deleting elements
numbers.remove(4)

# Using the array module

import array

#Creating an integer array
arr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(arr[0])        #Output: 1

# Modifying elements
arr[1] = 10

# Appending elements
arr.append(6)

# Deleting elements
arr.remove(3)

#Using NumgPy Arrays

import numpy as np

# Creating a Numpy array
np_array = np.array([1, 2, 3, 4, 5])

# Accessing elements
print(np_array[0])    #Output: 1

# Modifying elements
np_array[1] = 10

# Applying mathematical operations
np_array = np_array*2
print(np_array)           # Output: [2 20 6 8 10]

# Multidimensional arrays
# Example of 2D array:

# 2D (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][1]) #Output: 2 (row 0, column 1)

# Example of 3D Arrays:
array_3d = [
    [
        [1, 2, 3],     # 1st 2D array
        [4, 5, 6]
    ],
    [
        [7, 8, 9],     # 2nd 2D array
        [10, 11, 12]
    ]
]

# Accessing elements
print(array_3d[0][1][2])       #Output: 6 (1st 2D array, 2nd array, 2nd row, 3rd column)

#Operation on Multidimensional Arrays:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements at row 2, column 1
print(matrix[2][1]) #Output: 8

#Updating elements:

matrix[1][1] = 10      #Updating row 1, column 1 to 10
print(matrix)  #Output: [[1, 2, 3], [4, 10, 6], [7, 8, 9]]

# Using Libraries for Multidimensional Array

import numpy as np

# Creating a 2D array using NumPy
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing an element
print(matrix[0, 1])  #Output: 2

# Performing operations
print(matrix + 1)  # Adding 1 to each element