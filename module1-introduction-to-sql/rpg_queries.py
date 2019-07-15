#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('rpg_db.sqlite3')


# In[3]:


c = conn.cursor()


# In[4]:


character_count = c.execute('''SELECT COUNT(name) FROM charactercreator_character''');
character_count.fetchone()


# In[5]:


cleric_count = c.execute('''SELECT COUNT(character_ptr_id) FROM charactercreator_cleric''')
cleric_count.fetchone()


# In[6]:


fighter_count = c.execute('''SELECT COUNT(character_ptr_id) FROM charactercreator_fighter''')
fighter_count.fetchone()


# In[7]:


mage_count = c.execute('''SELECT COUNT(character_ptr_id) FROM charactercreator_mage''')
mage_count.fetchone()


# In[8]:


necromancer_count = c.execute('''SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer''')
necromancer_count.fetchone()


# In[9]:


thief_count = c.execute('''SELECT COUNT(character_ptr_id) FROM charactercreator_thief''')
thief_count.fetchone()


# In[10]:


item_count = c.execute('''SELECT COUNT(item_id) FROM armory_item''')
item_count.fetchone()


# In[11]:


weapon_count = c.execute('''SELECT COUNT(item_ptr_id) FROM armory_weapon''')
weapon_count.fetchone()


# In[12]:


not_weapon_count = c.execute('''
    SELECT COUNT(item_id)
    FROM armory_item
    WHERE NOT EXISTS 
    (SELECT * 
    FROM armory_weapon
    WHERE armory_weapon.item_ptr_id = armory_item.item_id);
    ''')
not_weapon_count.fetchone()


# In[44]:


character_inv_count = c.execute('''
    SELECT character_id, COUNT(item_id) 
    FROM charactercreator_character_inventory
    GROUP BY character_id 
    LIMIT 20''');
character_inv_count.fetchall()


# In[48]:


character_weapon_count = c.execute('''
    SELECT COUNT(item_id)
    FROM charactercreator_character_inventory
    WHERE NOT EXISTS 
    (SELECT * 
    FROM armory_weapon
    WHERE armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id)
    GROUP BY character_id
    LIMIT 20;''')
character_weapon_count.fetchall()


# In[45]:


character_item_average = c.execute('''
    SELECT AVG() FROM(SELECT COUNT(item_id) 
    FROM charactercreator_character_inventory
    GROUP BY character_id)
    LIMIT 20;''')


# In[33]:


character_item_average.fetchall()


# In[ ]:




