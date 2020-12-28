# Import Pandas using its common nickname
import pandas as pd

# Reading test_data.csv as a dataframe
df = pd.read_csv('test_data.csv')

# Adding another column for average scores
df['Average Score'] = (df['Math Score'] + df['Physics Score'] + df['Chemistry Score'] + df['English Score']) / 4
# Short Method
df['Short Method Average'] = (df.iloc[:, 2:6].sum(axis=1)) / 4

# Exporting into a separate csv file
df.to_csv('modified.csv', index = False)