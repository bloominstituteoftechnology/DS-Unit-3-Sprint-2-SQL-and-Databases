#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import pandas as pd


# In[8]:


conn = sqlite3.connect('Documents/Lambda School/Week 10/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')
c = conn.cursor()


# In[59]:


query1 = 'SELECT COUNT(*) FROM charactercreator_character;'
pd.read_sql(query1, conn)

# c.execute(query1)
# print(c.fetchone())


# In[61]:


query2 = ''' SELECT
            (SELECT COUNT(*) FROM charactercreator_mage) AS mage, 
            (SELECT COUNT(*) FROM charactercreator_thief) AS thief,
            (SELECT COUNT(*) FROM charactercreator_cleric) AS cleric,
            (SELECT COUNT(*) FROM charactercreator_fighter) AS fighter,
            (SELECT COUNT(*) FROM charactercreator_necromancer) AS necromancer;
         '''
pd.read_sql(query2, conn)

# c.execute(query2)
# print(c.fetchone())


# In[62]:


query3 = 'SELECT COUNT(*) FROM armory_item;'
pd.read_sql(query3, conn)

# c.execute(query3)
# print(c.fetchone())


# In[21]:


query4 = '''SELECT
            (SELECT COUNT(*) FROM armory_item, armory_weapon WHERE item_id = item_ptr_id),
            (SELECT COUNT(*) FROM armory_item, armory_weapon WHERE item_id <> item_ptr_id);
         '''
pd.read_sql(query4, conn)   

# c.execute(query4)
# print(c.fetchone())


# In[65]:


query5 =  '''
            SELECT COUNT(item_id) AS Num_Items
            FROM charactercreator_character_inventory
            GROUP BY character_id
            LIMIT 20
        
'''
pd.read_sql(query5, conn) 

# c.execute(query5)
# print(c.fetchall())


# In[48]:


query6 =  '''
            SELECT COUNT(item_id) AS Num_Items
            FROM charactercreator_character_inventory
            JOIN armory_weapon
            WHERE item_id = item_ptr_id
            GROUP BY character_id
            LIMIT 20
        
'''
pd.read_sql(query6, conn) 

# c.execute(query6)
# print(c.fetchall())


# In[56]:


query7 = '''
            SELECT AVG(items)

            FROM(
                SELECT COUNT(item_id) AS items
                FROM charactercreator_character_inventory
            GROUP BY character_id
            LIMIT 20
            )
            
        
'''

pd.read_sql(query7, conn)

# c.execute(query7)
# print(c.fetchone())


# In[57]:


query8 =  '''
            SELECT AVG(items)
            FROM(
                SELECT COUNT(item_id) AS items
            FROM charactercreator_character_inventory
            JOIN armory_weapon
            WHERE item_id = item_ptr_id
            GROUP BY character_id
            LIMIT 20
            )
        
'''
pd.read_sql(query8, conn) 

# c.execute(query8)
# print(c.fetchone())


# In[72]:


df = pd.read_csv('Documents/Lambda School/Week 10/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
df.shape
df.head()


# In[70]:


con = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review',con)


# In[71]:


query9 = 'SELECT COUNT(*) FROM review;'
pd.read_sql(query9, con)


# In[ ]:


query10 = '''   SELECT COUNT(*) 
                FROM review
                WHERE( Nature > 100, 
          '''
pd.read_sql(query10, con)

