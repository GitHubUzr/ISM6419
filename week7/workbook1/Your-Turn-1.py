## Your Turn 1
# import csv file into python data frame

# Data taken from http://census.ire.org/data/bulkdata.html
# State: Florida(12)
# Summary Level: State(040)
# Table: P2. URBAN AND RURAL
import pandas as pd
Location = "datasets/census.csv"
df = pd.read_csv(Location)
df.head()