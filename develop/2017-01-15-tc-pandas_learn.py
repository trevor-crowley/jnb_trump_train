
# coding: utf-8

# # Setup Notebook

# In[26]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[27]:

sns.set()
plt.rcParams['figure.figsize']=(12,8)


# In[28]:

# Find the notebook the saved figures came from
fig_prefix = "../figures/2017-01-15-tc-"


# ## Series test

# In[29]:

s = Series(np.random.randn(100))
#s[:20] =1


# In[30]:

plt.hist(s);
plt.savefig(fig_prefix + "histogram.png")


# In[31]:

sns.distplot(s);
plt.savefig(fig_prefix + "histogram_sns.png")


# In[ ]:



