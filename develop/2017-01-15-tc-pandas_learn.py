
# coding: utf-8

# # Setup Notebook

# In[9]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[35]:

sns.set()
plt.rcParams['figure.figsize']=(12,8)


# ## Series test

# In[103]:

s = Series(np.random.randn(10))
# s[:20] =1


# In[105]:

plt.hist(s);


# In[88]:




# In[ ]:



