#Your Turn
# create an age histogram categorized by gender
# (code built to work on jupyter notebook)

# import data
import matplotlib.pyplot as plt
import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

# create histogram
get_ipython().run_line_magic('matplotlib', 'inline')
df.hist(column="age", by="gender")
