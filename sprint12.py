#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 


# In[3]:


conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# In[4]:


create_t = """ 
CREATE TABLE demo (
            s varchar(10),
            x INT, 
            y INT
);
"""


# In[5]:


curs.execute(create_t)


# In[6]:


insert_t1 = """
INSERT INTO demo (s, x, y)
VALUES('g', '3', '9') 
;
"""


# In[7]:


insert_t2 = """
INSERT INTO demo (s, x, y)
VALUES('v', '5', '7') 
;
"""


# In[8]:


insert_t3 = """
INSERT INTO demo (s, x, y)
VALUES('f', '8', '7') 
;
"""


# In[9]:


curs.execute(insert_t1)
curs.execute(insert_t2)
curs.execute(insert_t3)


# In[10]:


curs.execute('SELECT * FROM demo'); 
curs.fetchall()
print([('g', 3, 9), ('v', 5, 7), ('f', 8, 7)])


# In[11]:


curs.execute('SELECT COUNT(*) FROM demo'); 
curs.fetchall()
print([(3,)])


# In[12]:


curs.execute('SELECT COUNT(*) FROM demo WHERE x>= 5 AND y>=5'); 
curs.fetchall()
print([(2,)])


# In[13]:


curs.execute('SELECT COUNT(DISTINCT(y)) from demo'); 
curs.fetchall()
print([(2,)])


# In[29]:


conn = sqlite3.connect('/Users/TomasFox/Downloads/northwind_small.sqlite3')
curs = conn.cursor()
curs


# In[44]:


query = """SELECT Product.ProductName, Product.UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10"""
curs.execute(query).fetchall()
print([('Côte de Blaye', 263.5),
 ('Thüringer Rostbratwurst', 123.79),
 ('Mishi Kobe Niku', 97),
 ("Sir Rodney's Marmalade", 81),
 ('Carnarvon Tigers', 62.5),
 ('Raclette Courdavault', 55),
 ('Manjimup Dried Apples', 53),
 ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46),
 ('Rössle Sauerkraut', 45.6)])


# In[43]:


query = """SELECT AVG(Employee.HireDate - Employee.BirthDate) FROM Employee"""
curs.execute(query).fetchall()
print([(37.22222222222222,)])


# In[42]:


query = """SELECT Employee.City, AVG(Employee.HireDate - Employee.BirthDate) FROM Employee
GROUP BY Employee.City"""
curs.execute(query).fetchall()
print(curs.execute(query).fetchall())


# In[41]:


query = """SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier on Product.SupplierId=Supplier.id
ORDER BY Product.UnitPrice DESC LIMIT 10"""
curs.execute(query).fetchall()
print([('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
 ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
 ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
 ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
 ('Raclette Courdavault', 55, 'Gai pâturage'),
 ('Manjimup Dried Apples', 53, "G'day, Mate"),
 ('Tarte au sucre', 49.3, "Forêts d'érables"),
 ('Ipoh Coffee', 46, 'Leka Trading'),
 ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')])


# In[38]:


query = """SELECT count(product.Id), Category.CategoryName
FROM PRODUCT 
JOIN Category ON Product.CategoryId=Category.Id
GROUP BY Category.CategoryName
ORDER BY COUNT(Product.Id) DESC
LIMIT 1
"""
curs.execute(query).fetchall()
print('13', 'confections')


# In[40]:


query = """SELECT Employee.Id, Employee.FirstName, Employee.LastName, COUNT(EmployeeTerritory.TerritoryId)
FROM Employee
JOIN EmployeeTerritory on Employee.Id=EmployeeTerritory.EmployeeId
GROUP BY Employee.FirstName
ORDER BY COUNT(EmployeeTerritory.Id) DESC 
LIMIT 1 """
curs.execute(query).fetchall()
print('7', 'Robert', 'King', '10')


# 1) There is a many-to-many relationship between the employee table and the territory table, in which 
#    employee territories behaves as a 'secondary' or 'intermediary table'
# 2) MongoDB is appropriate if we are tring to create relational databases that require scalability; Mongo allows you 
#    to work with many different 'workers' or computers in parallel that allow you to horizontally scale your workflow
# 3) 'NewSQL' is a new concept in which many different start-ups are simultaneously competing in order to make SQL more 
#     scalable as well as more efficient.
