import numpy as np
import matplotlib.pyplot as plt

# Creating an array that ranges from 0 to 5, and has an increment of 0.1 for each element 
x = np.arange(0, 20, 0.1) 

# Defining some functions of x
y1 = np.sin(x)	# Sine Function
y2 = np.cos(x)	# Cos Function
y3 = x			# Graph of y = x
y4 = x**2		# Graph of y = x^2

fig, axes = plt.subplots(2, 2) 		# Defining our figure's columns and rows

axes[0, 0].plot(x, y1, color = 'blue')
axes[0, 0].set(xlabel = 'X Axis', ylabel = 'Sine Function')

axes[0, 1].plot(x, y2, color = 'red')
axes[0, 1].set(xlabel = 'X Axis', ylabel = 'Cos Function')

axes[1, 0].plot(x, y3, color = 'green')
axes[1, 0].set(xlabel = 'X Axis', ylabel = 'Linear Function')

axes[1, 1].plot(x, y4, color = 'black')
axes[1, 1].set(xlabel = 'X Axis', ylabel = 'Quadratic Function')

plt.legend()
plt.show()