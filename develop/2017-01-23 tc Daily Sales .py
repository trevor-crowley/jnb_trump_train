
# coding: utf-8

# # Review DS new file format

# In[2]:

pwd


# In[3]:

import pandas as pd


# In[136]:

get_ipython().system('cat ../../zzData_RAW/header.txt | grep Name > ../../zzData_RAW/header2.txt')


# In[158]:

f = pd.read_table ('../../zzData_RAW/header2.txt', header=None )
cols = f.iloc[:,0].str.split('=').str.get(1)


# In[189]:

df_new = pd.read_table ('../../zzData_RAW/BRSalesNew.txt',header=None, index_col=[0,1,2],names=cols, dtype=object)
df_new.GLANI = df_new.GLANI.astype('str')


# In[191]:

df_new.head().T


# In[213]:

df_new.GLANI.unique


# In[ ]:



