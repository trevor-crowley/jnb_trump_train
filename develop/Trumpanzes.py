
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[3]:

donations = pd.read_csv('P00000001-ALL.csv', dtype='object')
donations['contb_receipt_amt'] = pd.to_numeric(donations['contb_receipt_amt'])
    


# In[ ]:

donations.groupby("cand_nm").median().sort_values("contb_receipt_amt").plot(kind='bar')


# In[ ]:

donations.dtypes


# In[33]:

pdonations = donations[['contbr_st', 'cand_nm', 'contbr_occupation', 'contb_receipt_amt']]


# In[43]:

pdonations.so


# In[50]:

donations['contbr_nm'].describe()


# In[51]:

ls


# In[56]:

donations.keys()
donations.values


# In[57]:

d = donations


# In[66]:

d.head(2).T


# In[124]:

d.groupby('cand_nm').sum().sort()


# In[125]:

2*2


# In[ ]:



