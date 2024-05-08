#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd


# In[79]:


df = pd.read_csv("Diabities Decision tree.csv")


# In[80]:


df.head()


# In[81]:


df.info()


# In[82]:


df.shape


# In[83]:


x = df.drop('Outcome',axis=1)


# In[84]:


x.head()


# In[85]:


y = df['Outcome']


# In[86]:


y


# In[87]:


from sklearn.model_selection import train_test_split


# In[88]:


X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.3 )


# In[89]:


X_train.shape


# In[90]:


X_test.shape


# In[91]:


from sklearn.tree import DecisionTreeClassifier


# In[92]:


model = DecisionTreeClassifier()


# In[93]:


model.fit(X_train, Y_train)


# In[94]:


Y_pred = model.predict(X_test)


# In[73]:


Y_test


# In[95]:


from sklearn import metrics


# In[96]:


print(metrics.accuracy_score(Y_test, Y_pred))


# In[76]:


df


# In[97]:


if model.predict([[123, 10, 122, 72, 48,49.6 ,0.539, 60]])[0] == 1:
  print("Having diabetes")
else:
  print("Not having diabetes")


# In[ ]:




