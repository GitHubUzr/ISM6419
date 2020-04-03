## Your Turn 2
# create a column that shows busy
# if a student exercises more than 3hrs/week
# and studies more than 17hrs/week

# load data from csv
import pandas as pd
import numpy as np
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
# create column
df['timemgmt'] = np.where((df['exercise']<3)
& (df['hours']<17),'busy', '')
df.tail(10)