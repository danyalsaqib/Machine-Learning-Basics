import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,10,12], [13,14,15,16]])
print("a:\n", a)
print("\nshape: ", a.shape)

#Remember when transforming an array into a different shape, the total number of elements don't change
b = a.reshape(2, 8)
print("\nb:\n", b)
print("\nshape: ", b.shape)

c = a.reshape(8, 2)
print("\nc:\n", c)
print("\nshape: ", c.shape)

d = a.reshape(1, 16)
print("\nd:\n", d)
print("\nshape: ", d.shape)

e = a.reshape(2, 2, 2, 2)
print("\ne:\n", e)
print("\nshape: ", e.shape)
