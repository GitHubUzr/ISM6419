#Your Turn
# create a scatter plot of the hours and grade data in datasets/gradedata.csv
# (code built for use in jupyter notebook)

# import data
import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

# create scatterplot
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# scatter(x,y)
# where hours column is x
# and grade column is y
plt.scatter(df['hours'], df['grade'])
# there is a general pattern;
# as number of hours studying increase
# so does the grade

