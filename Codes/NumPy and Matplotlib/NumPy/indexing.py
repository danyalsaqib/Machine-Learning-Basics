import numpy as np

# Define a function to get array information
def getarrayinfo(arr):				# Takes an array as input
	print("\n**********")
	print("array:\n", arr)				# Prints array
	print("dimensions: ", arr.ndim)	# Prints array dimensions
	print("shape: ", arr.shape)		# Prints array shape
	print("datatype: ", arr.dtype)	# Prints array datatype

# Creating an array
d = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype = np.int32)
getarrayinfo(d)

# Remember that indexes in Python start from 0
item12 = d[0, 1]
print("First Row, Second Column: ", item12)
item33 = d[2, 2]
print("Third Row, Third Column: ", item33)
item23 = d[1, 2]
print("Second Row, Third Column: ", item23)

row2 = d[1, :] 					# Using ':' gets all the elements in a row or column
print("Second Row: ", row2)
col3 = d[:, 2]
print("Third Column: ", col3)	# Extracting a column using the ':' operator