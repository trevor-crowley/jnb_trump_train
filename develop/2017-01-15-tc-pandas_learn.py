
# coding: utf-8

# # Setup Notebook

# In[2]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:

sns.set()
plt.rcParams['figure.figsize']=(12,8)


# In[9]:

# Find the notebook the saved figures came from
fig_prefix = "../figures/2017-01-15-tc-"


# ## Series test

# In[10]:

s = Series(np.random.randn(100))
# s[:20] =1


# In[11]:

plt.hist(s);
plt.savefig(fig_prefix + "histogram.png")


# In[88]:




# In[ ]:



