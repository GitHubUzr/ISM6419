#Your Turn
# Take the dataset and add an annotation to
# Bob's 76 that says “Wow!”]

import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
df = df.set_index(df['Names'])
df.plot()

# what we want the annotation to say
displayText = "Wow!"
xloc = 0.04
# as Bob is the only one with a 76
# 76 is the grade value we're looking for
yloc = 76
xtext = -10
ytext = 22
plt.annotate(displayText,xy=(xloc, yloc),xytext=(xtext,ytext),xycoords=('axes fraction', 'data'),
             textcoords='offset points', arrowprops=dict(facecolor='black',shrink=0.05))
