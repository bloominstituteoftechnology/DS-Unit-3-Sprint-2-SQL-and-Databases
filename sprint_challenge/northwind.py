#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[2]:


conn = sqlite3.connect('northwind_small.sqlite3')


# In[4]:


# What are the ten most expensive items (per unit price) in the database?
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT ProductName, UnitPrice 
                    FROM Product 
                    ORDER BY UnitPrice DESC
                    LIMIT 10;""")
    most_exp = curs.fetchall()
    print(most_exp)


# In[5]:


# What is the average age of an employee at the time of their hiring? 
# (Hint: a lot of arithmetic works with dates.)
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT AVG(birthdate - hiredate)
                    FROM Employee;""")
    avg_age = curs.fetchall()
    print(avg_age)


# In[6]:


# What are the ten most expensive items (per unit price)
# in the database and their suppliers?
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT ProductName, UnitPrice, CompanyName
                    FROM Product, Supplier
                    WHERE Product.SupplierId = Supplier.Id
                    ORDER BY UnitPrice DESC
                    LIMIT 10;""")
    suppliers_n_most_exp = curs.fetchall()
    print(suppliers_n_most_exp)


# In[7]:


# What is the largest category (by number of products in it)?
with conn:
    curs = conn.cursor()
    curs.execute("""SELECT CategoryName, Count(Product.CategoryId) as NumberOfProducts
                    FROM Category, Product
                    WHERE Category.Id = Product.CategoryId
                    GROUP BY CategoryName
                    ORDER BY NumberOfProducts DESC
                    LIMIT 1;""")
    largest_category = curs.fetchall()
    print(largest_category)

