#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[11]:


conn = sqlite3.connect('repos/tomfox1/SQL/module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()
curs.execute('SELECT * FROM charactercreator_character;').fetchall()


# In[13]:


curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()


# In[17]:


curs.execute("""SELECT  (
        SELECT COUNT(*)
        FROM   charactercreator_cleric
        ) AS num_cleric,
        (
        SELECT COUNT(*)
        FROM   charactercreator_fighter
        ) AS num_fighter,
        (
        SELECT COUNT(*)
        FROM   charactercreator_mage
        ) AS num_mage,
        (
        SELECT COUNT(*)
        FROM   charactercreator_necromancer
        ) AS num_necromancer,
        (
        SELECT COUNT(*)
        FROM   charactercreator_thief
        ) AS num_thief""").fetchall()


# In[19]:


curs.execute('SELECT COUNT(*) FROM armory_item;').fetchall()


# In[21]:


curs.execute("""SELECT COUNT (armory_weapon.item_ptr_id)
FROM armory_weapon""").fetchall()


# In[ ]:


#have to complete last 2 questions on averages 

