import numpy as np
import matplotlib.pyplot as plt

# Creating an array that ranges from 0 to 5, and has an increment of 0.1 for each element 
x = np.arange(0, 20, 0.4) 

# Plotting Sine function as stem plot
y = np.sin(x)

plt.stem(x, y, label = 'sin(x)')

plt.title('Sine Graph - Stem Plot')
plt.xlabel('x Axis')
plt.ylabel('Y Axis')

plt.legend()
plt.show()