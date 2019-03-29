#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sql 


# In[2]:


northwind = '/home/william/repos/wjarvis2/unit3_week2/northwind_small.sqlite3'


# In[3]:


conn = sql.connect(northwind)


# In[4]:


c = conn.cursor()


# In[5]:


c.execute('''SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10''')


# In[6]:


print ('10 Most Expensive Products in Descending Order:')
print (c.fetchall())


# In[7]:


c = conn.cursor()


# In[8]:


c.execute('''SELECT avg(HireDate - BirthDate) FROM Employee''')


# In[9]:


print ('Average age at hire:')
print (c.fetchall())


# In[10]:


c = conn.cursor()


# In[ ]:





# In[ ]:





# In[ ]:




