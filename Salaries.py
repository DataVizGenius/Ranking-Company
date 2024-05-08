#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dt = pd.read_csv ('Salaries.csv')


# In[2]:


dt.head()


# In[4]:


dt.columns


# In[12]:


dt.rename(columns={"sex":"gender","rank":"Prof","salary":"Earning"},inplace=True)


# In[13]:


dt.info()


# In[14]:


dt['gender'].unique()


# In[ ]:




