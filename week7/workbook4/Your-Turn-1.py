## Your Turn 1
# use bins to create a pass/fail column
# where 80 and above is passing

# load dataset
import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
# create the bin dividers
bins = [0, 80, 100]
# create names for the two groups
group_names = ['Fail', 'Pass']
# cut grades
df['pass/fail'] = pd.cut(df['grade'], bins,
labels=group_names)
df
