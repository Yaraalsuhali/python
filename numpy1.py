import numpy as np

# create a 20 array
my_array = np.array([[1, 2, 3,], [4, 5, 6,], [7, 8, 9,]])

# print th array
print(my_array)

# get the shape of the array 
print(my_array.shape)

# get the datatype of the array
print(my_array.dtype)

# preform some basic arithmetic on the array
result = my_array + 2
print(result)

# calculate the mean of the array
mean = np.mean(my_array)
print(mean)