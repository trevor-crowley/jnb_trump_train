
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
plt.rcParams['figure.figsize'] = (12, 8)
get_ipython().magic("config InlineBackend.figure_format='retina'")


# In[4]:

# Find the notebook the saved figures came from
fig_prefix = "../figures/2017-01-14-tc-"


# ## Load Data

# In[7]:

datfile = '../../zzData_RAW/P00000001-ALL.csv'

cols = ['cand_nm', 'contbr_st', 'contbr_employer',         'contb_receipt_amt', 'contbr_occupation', 'contb_receipt_amt', 'contb_receipt_dt']

donate = pd.read_csv(datfile, index_col=False, dtype='object', usecols = cols)
donate['contb_receipt_amt'] = pd.to_numeric(donate['contb_receipt_amt'])
# donate['contb_receipt_dt'] = pd.to_datetime(donate['contb_receipt_dt'])

donate.dtypes


# ## Review Data

# In[8]:

import qgrid # Best practices is to put imports at the top of the Notebook.
qgrid.nbinstall(overwrite=True)


# In[9]:

donate.head()


# In[10]:

qgrid.show_grid(donate.head(), remote_js=True)


# In[11]:

donate.groupby('cand_nm').mean()


# In[56]:

sns.stripplot(x="cand_nm", y="contb_receipt_amt", data=donate[10000:20000]);


# In[ ]:

#x = np.random.normal(size=100)
sns.distplot(donate['contb_receipt_amt'], bins=20, kde=False, rug=True);


# In[ ]:



