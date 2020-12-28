import numpy as np

# Creating an Array
a = np.array([1, 2, 3, 4, 5], dtype = np.float)
print("a: \n", a)

# Printing various element-wise operations
print("\na + 2: \n", a + 2)
print("\na - 4: \n", a - 4)
print("\na * 3: \n", a * 3)
print("\na / 5: \n", a / 5)

# Matrix element wise addition
b = np.ones(5)
print("\nb: \n", b)
print("\na + b: \n", a + b)

# Matrix element wise multiplication
c = np.array([2, 4, 6, 8, 10])
print("\nc: \n", c)
print("\na * c: \n", a * c)