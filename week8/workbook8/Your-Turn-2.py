#Your Turn
# create a pie chart on student demerits and
# rotate and edit chart settings so the student with the
# least number of demerits (John) is being highlighted
# (code built to work on jupyter notebook)

# create data
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)

# add a column for total violations/demerit per student
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']

# create a custom pie chart
plt.pie(df['TotalDemerits'],
# add students names as labels
        labels=df['Names'],
# explodes out pie pieces above 0
# john's is the 4th pie piece
        explode=(0,0,0,0.2,0),
# rotate the pie chart to different points
        startangle=240,
# format numeric labels to pie pieces
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()
