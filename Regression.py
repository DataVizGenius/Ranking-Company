#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import pandas as pd


# In[5]:


import pylab as pl


# In[6]:


import numpy as np


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df=pd.read_csv('FuelConsumption.csv')


# In[9]:


df.head()


# In[10]:


df.describe()


# In[11]:


df.columns


# In[14]:


cdf=df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(15)


# In[15]:


viz=cdf[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
viz.hist()
plt.show()


# In[20]:


plt.scatter(cdf.FUELCONSUMPTION_COMB,cdf.CO2EMISSIONS,color='Green')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()


# In[22]:


plt.scatter(cdf.ENGINESIZE,cdf.CO2EMISSIONS,color='orange')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


# In[24]:


plt.scatter(cdf.CYLINDERS,cdf.CO2EMISSIONS,color='red')
plt.xlabel("'CYLINDERS'")
plt.ylabel("Emission")
plt.show()


# In[25]:


msk = np.random.rand(len(df))<0.8
msk
train=cdf[msk]
test= cdf [~msk]


# In[26]:


plt.scatter (train.ENGINESIZE,train.CO2EMISSIONS, color='red')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


# In[27]:


from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)


# In[28]:


plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")


# In[29]:


from sklearn import linear_model
regr = linear_model.LinearRegression()
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
regr.fit(test_x, test_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)


# In[30]:


viz.corr()


# In[ ]:




