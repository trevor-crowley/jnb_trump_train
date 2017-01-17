
# coding: utf-8

# ## Load DCC Data

# In[144]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[145]:

dfile = '../../zzData_RAW/2017-01-16-tc-dcc-scrub/order_comment.txt'
hfile = '../../zzData_RAW/2017-01-16-tc-dcc-scrub/backorder.FDF'


# In[146]:

get_ipython().getoutput('head -2 $dfile')
#!!cat $hfile


# In[147]:

cols = ['doc_no','doc_type','line_id','seq_id','note_line','bill_to',        'shipto', 'order_date','ship_to']
cols


# In[148]:

df = pd.read_table(dfile, encoding='latin1', header=0, names=cols,                   usecols=[0,1,3,4,7] )


# In[149]:

df.head()


# ## Scrub

# In[150]:

df.seq_id = np.trunc(df.seq_id * 100)
df.seq_id = df.seq_id.astype(int)
df.note_line = df.note_line.str.lstrip('&')


# In[151]:

df.head()


# ## Consolidate TBD

# In[178]:

df.seq_id[68]


# In[194]:

df.to_csv('../data/dcc_order_comment.txt', sep='\t' )


# In[195]:

ls -lah ../data/dcc_order_comment.txt


# In[ ]:



