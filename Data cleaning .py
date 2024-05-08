#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
dt = pd.read_csv('diabetes_unclean.csv')


# In[18]:


dt.head()


# In[5]:


dt.info()


# In[7]:


dt.columns


# In[15]:


dt.rename(columns={"No_Pation":"Patient_No"},inplace=True)


# In[16]:


dt.info()


# In[17]:


dt.isnull().sum()


# In[7]:


mean_value=dt['HbA1c'].mean()
mean_value 


# In[8]:


dt['HbA1c'].fillna (mean_value,inplace=false)


# In[10]:


#check the null places
dt.isnull().sum()


# In[9]:


dt1=dt.dropna()


# In[10]:


dt1.isnull().sum()


# In[11]:


dt1.groupby('CLASS')['CLASS'].agg("count")


# In[12]:


dt['CLASS'].unique()


# In[15]:


dt1['CLASS']=dt1['CLASS'].str.replace('Y ','Y')
dt1['CLASS']=dt1['CLASS'].str.replace('N ','N')


# In[17]:


dt1['CLASS'].unique()


# In[19]:


dt1.describe()


# In[ ]:




