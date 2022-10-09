#!/usr/bin/env python
# coding: utf-8

# ## Assignment -  1

# ###  Import the necessary libraries

# In[55]:


import pandas as pd
import requests
import numpy as np


# ###  Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). <br>
# Use sep= "|" while reading the data

# In[15]:



df=pd.read_csv('users.csv')
df.head()


# ### Assign it to a variable called users and use the 'user_id' as index

# In[20]:


users=pd.DataFrame(df)
users=users.set_index('user_id')


# In[21]:


print(users)
users.count()


# ### See the first 10 and last 10 entries 

# In[22]:


print("-------first 10 entries--------")
print(users.head(10))
print("-------last 10 entries--------")
print(users.tail(10))


# In[ ]:





# ### What is the number of observations in the dataset?

# In[35]:


print("number of observations are : " ,len(users))


# ### What is the number of columns in the dataset?

# In[37]:


print("number of columns : " , len(users.axes[1]))


# ### Print the name of all the columns.

# In[39]:


column_names=list(users.columns)
print(column_names)


# ### How is the dataset indexed?

# In[40]:


users.index


# ### What is the data type of each column?

# In[42]:


users.info()


# ### Print only the occupation column

# In[43]:


print(users['occupation'])


# ### How many different occupations are in this dataset?

# In[48]:


print("unique values of occupation is : " , users['occupation'].nunique())


# ### What is the most frequent occupation?

# In[49]:


print("most frequent value in users occupation : ", users['occupation'].mode())


# ###  DataFrame Info.

# In[50]:


users.info()


# ### Describe all the columns

# In[58]:


print(users.describe())
print(users.describe(exclude=[np.number]))


# ### Summarize only the occupation column

# In[64]:


users.occupation.value_counts()


# ###  What is the mean age of users?

# In[60]:


print(users['age'].mean())


# ###  What is the age with least occurrence?

# In[61]:


users['age'].value_counts().idxmin()


# In[ ]:




