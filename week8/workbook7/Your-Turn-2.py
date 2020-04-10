#Your Turn
# Create a bar plot showing grades over status

import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(status,grades)
df = pd.DataFrame(data = GradeList,columns=['Status', 'Grades'])
df = df.groupby('Status').mean()
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


