#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sql 


# In[2]:


northwind = '/home/william/repos/wjarvis2/unit3_week2/northwind_small.sqlite3'


# In[3]:


conn = sql.connect(northwind)


# In[24]:


c = conn.cursor()


# In[25]:


c.execute('''SELECT DISTINCT ProductName, UnitPrice, CompanyName FROM Product CROSS JOIN Supplier ON Supplier.ID = Product.SupplierID ORDER BY UnitPrice DESC LIMIT 10''')


# In[26]:


print ('10 Most expensive products by name, price, and supplier name:')
print (c.fetchall())


# In[78]:


c = conn.cursor()


# In[79]:


print ('10 largest categories by unique product ID counts:')

c.execute('''SELECT DISTINCT CategoryName FROM Category INNER JOIN Product ON Product.ID = Category.ID GROUP BY Category.ID LIMIT 10''')


# In[80]:


print (c.fetchall())


# In[ ]:





# In[ ]:




