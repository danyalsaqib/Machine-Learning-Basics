import numpy as np
import matplotlib.pyplot as plt

# Creating an array that ranges from 0 to 5, and has an increment of 0.1 for each element 
x = np.arange(0, 5, 0.1) 

# Taking sine of array x
y = np.sin(x)

# Plotting and showing results
plt.plot(x, y)
plt.show()