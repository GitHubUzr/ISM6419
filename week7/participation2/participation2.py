#!/usr/bin/env python
# coding: utf-8

# In[103]:


# download and gather data from past seven days not including today

# combine data from several csv files into single dataframe
import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("2020*.csv"):
    df = pd.read_csv(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.head()


# In[104]:


# filter for florida data
all_data = all_data.loc[all_data['Province_State'] == "Florida"]


# In[105]:


eod = pd.unique(all_data['Last_Update'])


# In[106]:


confirmed = []
# for each unique end of day value
for d in eod:
    # look only at rows for that day
    x = all_data.loc[all_data['Last_Update'] == d]
    # summarize column values for that day
    y = x.sum()
    # store summarized # of confirmed cases for each day in list
    confirmed.append(y.loc['Confirmed'])
# create new dataframe
CaseList = zip(eod,confirmed)
df = pd.DataFrame(data = CaseList, columns=['Last_Update','Confirmed'])
df.set_index('Last_Update',drop=True,inplace=True)
df


# In[107]:


import matplotlib.pyplot as plt
import matplotlib.ticker
df.plot.bar()
plt.title('Confirmed Cases in Florida')
plt.xlabel('Past Week')
#change y-axis to thousands
ax = plt.axes()
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.show()