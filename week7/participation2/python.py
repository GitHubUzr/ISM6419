#!/usr/bin/env python
# coding: utf-8

# In[33]:


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


# In[34]:


# filter for florida data
all_data = all_data.loc[all_data['Province_State'] == "Florida"]


# In[45]:


eod = pd.unique(all_data['Last_Update'])


# In[ ]:


# for each unique end of day value
for d in eod:
    # look only at rows for that day
    x = all_data.loc[all_data['Last_Update'] == d]
    # summarize column values for that day
    y = x.sum()
    # grab summarized # of confirmed cases for each day
    y.loc['Confirmed']
    # store in object




