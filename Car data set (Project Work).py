#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


dt = pd.read_csv ('CarData.csv')


# In[7]:


dt.head(5)


# In[8]:


import numpy as np
dt.replace ('?', np.nan,inplace= True)
dt.head()


# In[9]:


missing_data=dt.isnull()
missing_data.head()


# In[10]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[12]:


dt.columns


# In[13]:


avg_norm_loss=dt["normalized-losses"].astype ("float").mean(axis=0)
print(avg_norm_loss)


# In[14]:


dt["normalized-losses"].replace(np.nan, avg_norm_loss, inplace = True)


# In[15]:


dt.head ()


# In[16]:


dt1=dt.dropna()


# In[17]:


dt1.isnull().sum()


# In[18]:


dt[["bore", "stroke"]]= dt[["bore","stroke"]].astype("float")


# In[19]:


dt.head()


# In[20]:


dt.dtypes


# In[21]:


dt.head()


# In[22]:


# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
dt['city-L/100km'] = 235/dt["city-mpg"]

# check your transformed data 
dt.head()


# In[23]:


ak = dt


# In[24]:


ak.head ()


# In[25]:


# replace (original value) by (original value)/(maximum value)
ak['length'] = ak['length']/ak['length'].max()
ak['width'] = ak['width']/ak['width'].max()


# In[26]:


ak.head()


# In[27]:


ak.columns


# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(ak ["wheel-base"])


# In[45]:


type ("bore")


# In[49]:


['bore'].value_counts('str')


# In[50]:


import numpy as np


# In[51]:


group_names = ['Low', 'Medium', 'High']


# In[34]:


ak['wheel-base']


# In[48]:


ak['bore']


# In[36]:


ak["wheel-base"].value_counts()


# In[137]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, ak["wheel-base"].value_counts())


# In[138]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot


# In[37]:


ak.columns


# In[38]:


import pandas as pd


# In[39]:


dummy_variable_1 = pd.get_dummies(ak["fuel-type"])
dummy_variable_1.head()


# In[ ]:




