# Import Pandas using its common nickname
import pandas as pd

# Reading test_data.csv as a dataframe
df = pd.read_csv('test_data.csv')

# Adding another column for average scores
df['Average Score'] = (df['Math Score'] + df['Physics Score'] + df['Chemistry Score'] + df['English Score']) / 4
print(df[['Student Name', 'Average Score']])