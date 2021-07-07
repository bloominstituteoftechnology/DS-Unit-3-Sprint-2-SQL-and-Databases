#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd


# In[2]:


conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()


# In[6]:


query1 = 'SELECT COUNT(*) FROM charactercreator_character;'
answer1 = cursor.execute(query1).fetchone()[0]
print(answer1, 'total characters')


# In[ ]:


# There are 5 character subclasses from looking at the database
# Not sure how to count them in SQL
# They all start with 'charactercreator_' but so do two other databases that aren't subclasses


# In[7]:


query2 = 'SELECT COUNT(*) FROM armory_item;'
answer2 = cursor.execute(query2).fetchone()[0]
print(answer2, 'total items')


# In[8]:


query3 = 'SELECT COUNT(*) FROM armory_weapon;'
answer3 = cursor.execute(query3).fetchone()[0]
print(answer3, 'of the items are weapons and', answer2 - answer3, 'items are not weapons')


# In[13]:


query4 = 'SELECT COUNT(*), character_id         FROM charactercreator_character_inventory         GROUP BY character_id LIMIT 20;'
print('How many items each character has, top 20 rows:')
# print(cursor.execute(query4).fetchall()[1])
# Didn't work
answer = pd.read_sql(query4, conn)
answer = answer.set_index('character_id')
print(answer)


# In[14]:


# Not sure how to find out character weapon amount
# Strategy would be to check character_inventory against armory_weapon IDs


# In[15]:


# Come back to next two questions


# In[16]:


conn.commit()
conn.close()


# In[ ]:




