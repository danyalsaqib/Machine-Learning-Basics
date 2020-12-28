import numpy as np

# Trying to create a copy
a = np.array([1, 2, 3])
b = a
b[0] = 100
print("b: ", b)
print("a: ", a)
print("\nThis is because the '=' operator does not actually make a copy, but just tells NumPy that b points to the same thing that a does. Thus to make a proper copy, we have to use the 'copy()' command:\n")
# Making copy the proper way
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print("b: ", b)
print("a: ", a)