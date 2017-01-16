
# coding: utf-8

# # Setup Notebook

# In[16]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[17]:

sns.set()
plt.rcParams['figure.figsize']=(12,8)


# In[18]:

# Find the notebook the saved figures came from
fig_prefix = "../figures/2017-01-15-tc-"


# ## Series test

# In[23]:

s = Series(np.random.randn(100))
#s[:20] =1


# In[24]:

plt.hist(s);
plt.savefig(fig_prefix + "histogram.png")


# In[25]:

sns.distplot(s);
plt.savefig(fig_prefix + "histogram_sns.png")


# In[ ]:



