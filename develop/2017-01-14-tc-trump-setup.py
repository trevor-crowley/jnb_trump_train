
# coding: utf-8

# # Setup Notebook

# In[2]:

# Standard library
import os
import sys
sys.path.append("../src/")

# Third party imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[3]:

# Customizations
sns.set() # matplotlib defaults

# Any tweaks that normally go in .matplotlibrc, etc., should explicitly go here
plt.rcParams['figure.figsize'] = (12, 12)


# In[14]:

# Find the notebook the saved figures came from
fig_prefix = "../figures/2017-01-14-tc-"


# ## Load Data

# In[36]:

get_ipython().system('head -n2 ../data/P00000001-ALL.csv')


# In[40]:

cols = ['cand_nm', 'contbr_st', 'contbr_employer',         'contb_receipt_amt', 'contbr_occupation', 'contb_receipt_amt', 'contb_receipt_dt']
donate = pd.read_csv('../data/P00000001-ALL.csv', index_col=False, dtype='object', usecols = cols)
donate['contb_receipt_amt'] = pd.to_numeric(donate['contb_receipt_amt'])
# donate['contb_receipt_dt'] = pd.to_datetime(donate['contb_receipt_dt'])

donate.dtypes


# In[42]:

donate['contb_receipt_dt'].


# In[ ]:



