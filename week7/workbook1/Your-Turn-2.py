## Your Turn 2
# import excel file into python data frame

# Data taken from https://www.census.gov/library/publications/2011/compendia/usa-counties-2011.html
# Earnings, Total and Selected Industries (Bureau of Economic Analysis) — SIC
import pandas as pd
Location = "datasets/census.xls"
df = pd.read_excel(Location,sheet_name='Sheet1')
df.head()

df2 = pd.read_excel(Location,sheet_name='Sheet2')
df2.head()

