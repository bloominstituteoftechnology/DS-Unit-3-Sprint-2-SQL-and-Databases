#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3

conn = sqlite3.connect('repos/tomfox1/SQL/module1-introduction-to-sql/buddymove_holidayiq.sqlite3')
curs = conn.cursor()
curs.execute('SELECT * FROM review;').fetchall()


# In[5]:


curs.execute('SELECT COUNT(*) FROM review;').fetchall()


# In[18]:


curs.execute("""SELECT review.Nature, review.Religious FROM review
WHERE review.Nature >= 100 AND review.Religious >= 100""").fetchall()


# In[ ]:




