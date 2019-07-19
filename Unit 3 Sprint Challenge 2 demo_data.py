#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('demo_data.sqlite3')


# In[3]:


cursor = conn.cursor()


# In[4]:


cursor.execute('''CREATE TABLE demo_data
        (S TEXT PRIMARY KEY    NOT NULL,
        X INT    NOT NULL,
        Y INT    NOT NULL);''')


# In[5]:


cursor.execute("INSERT INTO demo_data (S, X, Y)         VALUES('G', 3, 9)");
cursor.execute('''INSERT INTO demo_data (S, X, Y)         VALUES('V', 5, 7)''');
cursor.execute('''INSERT INTO demo_data (S, X, Y)         VALUES('F', 8, 7)''');
conn.commit()


# In[12]:


for col in cursor.execute("SELECT * FROM demo_data"):
    print('S =', col[0])
    
conn.commit()


# In[29]:


for x in cursor.execute('''SELECT * FROM demo_data WHERE X >= 5 AND Y >= 5'''):
    print('X & Y > 5 =', x )


# In[33]:


for y in cursor.execute('''SELECT DISTINCT Y FROM demo_data'''):
    print('unique Y = ', y)


# In[ ]:




