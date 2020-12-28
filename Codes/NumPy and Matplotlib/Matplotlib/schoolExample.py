import numpy as np
import matplotlib.pyplot as plt

# Scores for School 1
math_scores_1 = np.array([78, 93, 54, 91, 82, 98])
english_scores_1 = np.array([81, 65, 70, 68, 79, 94])

# Scores for School 2
math_scores_2 = np.array([80, 72, 86, 71, 62, 84])
english_scores_2 = np.array([83, 80, 89, 98, 87, 95])

# Scatter Plot for both schools
plt.scatter(math_scores_1, english_scores_1, label = 'School 1', color = 'red', marker = 'o')
plt.scatter(math_scores_2, english_scores_2, label = 'School 2', color = 'blue', marker = 'x')

# Setting axis ranges from 60 to 100
plt.xlim(60, 100)
plt.ylim(60, 100)

# Making it look good
plt.title('Student Scores')
plt.xlabel('Math Scores')
plt.ylabel('English Scores')

plt.legend(loc = 'lower left')
plt.show()