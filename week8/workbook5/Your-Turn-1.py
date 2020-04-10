# load dataset from CSV
import pandas as pd
import numpy as np
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

# random sample of 500 rows from dataframe
df.take(np.random.permutation(len(df))[:500])
