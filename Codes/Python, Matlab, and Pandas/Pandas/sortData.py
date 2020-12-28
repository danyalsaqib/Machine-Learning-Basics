# Import Pandas using its common nickname
import pandas as pd

# Reading test_data.csv as a dataframe
df = pd.read_csv('test_data.csv')
# Find useful characteristics about your data
eng = df.sort_values('English Score')
# Only print their Names, IDs, and English scores
print(eng[['Student Name', 'Student ID', 'English Score']])