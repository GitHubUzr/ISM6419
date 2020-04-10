#Sorting
# load data
import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# sort dataframe by name, age, grade
df = df.sort_values(by=['lname','fname','age','grade'], ascending=[True,True,True,False])
df.head()
