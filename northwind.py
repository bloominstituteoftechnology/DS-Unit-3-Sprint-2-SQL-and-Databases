# !env/bin/python

"""Part 1 is demo_data.py"""
"""Part 2"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

"""
Question: What are the ten most expensive items in the DB?
"""
query = """
SELECT UnitPrice FROM Product 
ORDER BY UnitPrice DESC
LIMIT 10;
"""
cur.execute(query).fetchall()
"""
Answer: [(263.5,), (123.79,), (97,), (81,), (62.5,), (55,), (53,), (49.3,), (46,), (45.6,)]
"""

"""
Question: What is the avg age of an employee at the time of their hiring?
"""
query = """
SELECT AVG(HireDate - BirthDate)
FROM Employee;
"""
cur.execute(query).fetchall()
"""
Answer: 37.22
"""

"""Part 3"""

"""Question: What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?"""
query = """
SELECT UnitPrice, CompanyName FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
"""
cur.execute(query).fetchall()
 """Answer:
 [(263.5, 'Aux joyeux ecclésiastiques'), (123.79, 'Plutzer Lebensmittelgroßmärkte AG'), (97, 'Tokyo Traders'), (81, 'Specialty Biscuits, Ltd.'), (62.5, 'Pavlova, Ltd.'), (55, 'Gai pâturage'), (53, "G'day, Mate"), (49.3, "Forêts d'érables"), (46, 'Leka Trading'), (45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
 """

 """Question: What is the largest category?"""
query = """
SELECT COUNT(CategoryName), CategoryName AS cat
FROM Product
JOIN Category ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY COUNT(CategoryName) DESC;
"""
cur.execute(query).fetchall()
"""Answer:
[(13, 'Confections'), (12, 'Beverages'), (12, 'Condiments'), (12, 'Seafood'), (10, 'Dairy Products'), (7, 'Grains/Cereals'), (6, 'Meat/Poultry'), (5, 'Produce')]
"""


 """Part 4"""
 """These answers are also in the challenge.md file"""
 """
 Question: In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?


 Answer: Because more than many employees can be linked up with many different 
 territories it is a MANY-TO-MANY relationship.

 Question: What is a situation where a document store (like MongoDB) is appropriate?

 Answer: MongoDB is a document-oriented database system and you can think of it as "JSON in
 the cloud" which allows for huge amounts of data to be stored in a database.  
 It's appropriate for situations where you don't know the schema of your data beforehand,
 so more directed towards start-ups with minimum viable products.

 Question: When is MongoDB not appropriate?

 Answer: MongoDB is not appropriate where you do need to know the schema of your data, and
 for which you will be making complicated queries for and where for which the queries are
 somewhat guaranteed to return obvious results even if changes are made to the database.  
 So MongoDb definitely would not be appropriate for organizations like banks and large
 corporations.













