#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Demonstration of Seaborn library
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('classic')
plt.style.use('seaborn-whitegrid')
# Create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],
size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
# Plot the data with seaborn
sns.distplot(data['x'])
sns.distplot(data['y'])


# In[2]:


for col in 'xy':
    sns.kdeplot(data[col], shade=True)


# In[3]:


sns.kdeplot(data);


# In[4]:


with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde');


# In[5]:


with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')


# In[6]:


sns.pairplot(data);

