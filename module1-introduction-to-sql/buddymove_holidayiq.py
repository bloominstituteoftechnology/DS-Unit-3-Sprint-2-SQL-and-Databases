#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/mmastin/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')


# In[3]:


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
# Creating empty SQL database to be populated


# In[4]:


df.to_sql('holiday', con=conn, if_exists='replace')
# Populating database with CSV data


# In[5]:


cursor = conn.cursor()


# In[17]:


query = 'SELECT COUNT(*) FROM holiday;'
cursor.execute(query)
rowcount = cursor.fetchone()[0]
conn.commit()
# Not sure why I need 'fetchone' or if conn.commit() is necessary; found on stack overflow
# But it works!


# In[18]:


print(rowcount)


# In[22]:


query = 'SELECT COUNT(*) FROM holiday         WHERE ((Nature >= 100) & (Shopping >= 100));'
answer = cursor.execute(query).fetchone()[0]
print(answer, 'users reviewed at least 100 Nature and 100 Shopping')


# In[25]:


sports_average = cursor.execute('SELECT AVG(Sports) FROM holiday').fetchone()[0]
print('Average Sports reviews:', sports_average)
# Testing function


# In[26]:


religious_average = cursor.execute('SELECT AVG(Religious) FROM holiday').fetchone()[0]
nature_average = cursor.execute('SELECT AVG(Nature) FROM holiday').fetchone()[0]
theatre_average = cursor.execute('SELECT AVG(Theatre) FROM holiday').fetchone()[0]
shopping_average = cursor.execute('SELECT AVG(Shopping) FROM holiday').fetchone()[0]
picnic_average = cursor.execute('SELECT AVG(Picnic) FROM holiday').fetchone()[0]

print('Average religious reviews:', religious_average)
print('Average nature reviews:', nature_average)
print('Average theatre reviews:', theatre_average)
print('Average shopping reviews:', shopping_average)
print('Average picnic reviews:', picnic_average)
# Repeating function for other categories


# In[27]:


conn.commit()
conn.close()


# In[ ]:




