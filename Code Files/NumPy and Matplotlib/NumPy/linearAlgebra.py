import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("a:\n", a)

b = np.array([[5,4], [3,2], [1,0]])
print("\nb:\n", b)

# Remember that for matrix multiplication, the number of columns of first matrix should be equal to the number of rows of second matrix
c = np.matmul(a, b)
print("\nc:\n", c)

# Multiplying with identity matrix
i = np.identity(3)
print("\ni:\n", i)
m = np.matmul(a, i)
print("\nm:\n", m)