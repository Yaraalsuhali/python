import numpy as np 

# create a random 3x3 matrix
matrix = np.random.rand(3, 3)

print("original matrix:")
print(matrix)

# calculate the sum of all elements in the matrix
sum_of_elements = np.sum(matrix)
print("\nsum of all elements:", sum_of_elements)

# calculate the mean of each column
mean_of_columns = np.mean(matrix, axis=0)
print("\nmean of each column:")
print(mean_of_columns)

# elements-wise multiplication of the matrix by 2
matrix_times_2 = matrix * 2
print("\nmatrix multiplied by 2:")
print(matrix_times_2)