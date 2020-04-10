#Regression
# load data
import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()

# add gender as a numerical column to regression
# 1 = female
# 0 = male
import numpy as np
df['gender_num'] = np.where(df['gender']=='female',1,0)
df.tail(10)
import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender_num',data=df).fit()
result.summary()
# adj. r-squared value is the same
# p-value for gender is above 0.05
# we would not want to keep it in the regression model

