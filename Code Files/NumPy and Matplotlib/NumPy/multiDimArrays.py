import numpy as np

# Define a function to get array information
def getarrayinfo(arr):				# Takes an array as input
	print("\n**********")
	print("array:\n", arr)				# Prints array
	print("dimensions: ", arr.ndim)	# Prints array dimensions
	print("shape: ", arr.shape)		# Prints array shape
	print("datatype: ", arr.dtype)	# Prints array datatype

a = np.array([1,2,3])
getarrayinfo(a)

b = np.array([[1,2,3], [4,5,6]])
getarrayinfo(b)

c = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype = float)
getarrayinfo(c)

d = np.array([[[1,2,3]], [[4,5,6]], [[7,8,9]]], dtype = np.int32)
getarrayinfo(d)