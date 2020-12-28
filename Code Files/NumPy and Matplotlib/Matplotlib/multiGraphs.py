import numpy as np
import matplotlib.pyplot as plt

# Creating an array that ranges from 0 to 5, and has an increment of 0.1 for each element 
x = np.arange(0, 5, 0.1) 

# Taking sine of array x
y = np.sin(x)

# Plotting Sine of x
plt.plot(x, y, label = 'sin(x)', color = 'blue', linestyle = '-')

# Plotting Cosine of x
z = np.cos(x)
plt.plot(x, z, label = 'cos(x)', color = 'red', linestyle = '--')

plt.title('Sine and Cos Graphs')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend()
plt.show()