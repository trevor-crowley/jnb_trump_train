
# coding: utf-8

# In[1]:

import ipywidgets


# In[3]:

import jupyter_contrib_nbextensions


# In[4]:

import pyparsing


# In[4]:

import mkl


# In[6]:

import mpld3


# In[14]:

import scikitlearn


# In[2]:

import scikit-learn


# In[14]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state


# In[5]:

import sympy


# In[6]:

import cython


# In[7]:

import statsmodels


# In[8]:

import tqdm


# In[15]:

packages='''jupyter
notebook
pyparsing
matplotlib
mpld3
seaborn
pip
pandas
scipy
numpy
statsmodels
tqdm'''


# In[4]:

packages


# In[8]:

get_ipython().system('conda install -qy mkl')


# In[16]:

for p in  packages.split('\n') : 
    print (p)
    module = __import__ (p)


# In[17]:

import mpld3


# In[ ]:



