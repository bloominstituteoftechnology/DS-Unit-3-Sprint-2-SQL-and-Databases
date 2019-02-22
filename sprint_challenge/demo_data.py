#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[12]:


conn = sqlite3.connect('demo_data1.sqlite3')


# In[13]:


# Creating empty table `demo`
with conn:
    curs = conn.cursor()
    curs.execute("CREATE TABLE demo(s TEXT, x INT, y INT);")


# In[14]:


# Inserting values
with conn:
    curs = conn.cursor()
    curs.execute("INSERT INTO demo(s, x, y) VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);")


# In[16]:


# How many rows are there where both x and y are at least 5?
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT COUNT(*)
                    FROM demo;""")
    num_rows = curs.fetchall()
    print(num_rows)


# In[17]:


# Count how many rows you have - it should be 3!
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT COUNT(*)
                    FROM demo
                    WHERE x >= 5 and y >=5;""")
    five_or_above = curs.fetchall()
    print(five_or_above)


# In[19]:


# How many unique values of y are there 
# (hint - COUNT() can accept a keyword DISTINCT)
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT COUNT(DISTINCT(y))
                    FROM demo;""")
    y_distinct = curs.fetchall()
    print(y_distinct)


# In[ ]:




