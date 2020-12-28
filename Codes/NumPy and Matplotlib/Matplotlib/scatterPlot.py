import numpy as np
import matplotlib.pyplot as plt

math_scores = np.array([78, 93, 54, 91, 82, 98])
english_scores = np.array([81, 65, 70, 68, 79, 94])

# Scatter Plot
plt.scatter(math_scores, english_scores, color = 'red')

# Setting axis ranges from 60 to 100
plt.xlim(60, 100)
plt.ylim(60, 100)

# Making it look good
plt.title('Student Scores')
plt.xlabel('Math Scores')
plt.ylabel('English Scores')

plt.show()