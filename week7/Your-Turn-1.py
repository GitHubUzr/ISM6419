## Your Turn 1

import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])

# change out of bounds grade (below 0) to 0
df.loc[(df['Grades'] <= 0,'Grades')] = 0
df