#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('Northwind_small.sqlite')


# In[3]:


cursor = conn.cursor()


# In[4]:


cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
conn.commit()


# In[5]:


cursor.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n"CompanyName" VARCHAR(8000) NULL,"ContactName" VARCHAR(8000) NULL, \n"ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000) NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
conn.commit()


# In[46]:


for UnitPrice in cursor.execute('''SELECT DISTINCT UnitPrice FROM OrderDetail ORDER BY UnitPrice DESC LIMIT 10;'''):
    print('Most Expenisve : ', UnitPrice)


# In[58]:


for HireDate in cursor.execute('''SELECT BirthDate, HireDate,DATEDIFF(HireDate,BirthDate) AS difference from Employee'''):
    print('Average Age Hired:', HireDate)


# In[ ]:




