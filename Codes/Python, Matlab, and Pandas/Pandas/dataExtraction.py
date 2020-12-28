# Import Pandas using its common nickname
import pandas as pd

# Reading test_data.csv as a dataframe
df = pd.read_csv('test_data.csv')
# Reading Headings
print("Headings/Column Names: \n", df.columns)
# Accessing a specific column
print("\nNames: \n", df['Student Name'])
# Accessing a specific row
print("\nStudent 2 Info: \n", df.iloc[1])
# Accessing a specific item
print("\nStudent 10 Physics score: \n", df.iloc[9, 3])
# Finding students whose Math scores are over 80
mth = df.loc[df['Math Score'] > 80]
# Printing only their names, Student IDs, and Math scores
print("\nStudent with Math scores greater than 80:  \n", mth[['Student Name', 'Student ID', 'Math Score']])