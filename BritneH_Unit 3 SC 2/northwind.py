import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
conn.commit()

'''
What are the ten most expensive items (per unit price) in the database?
'''
most_expensive = '''
SELECT * 
FROM Product
ORDER BY UnitPrice DESC 
LIMIT 10;
'''
curs.execute(most_expensive)

'''
What is the average age of an employee at the time of their hiring?
'''
avg_age ='''
SELECT AVG(HireDate - BirthDate)
FROM Employee;
'''
curs.execute(avg_age)

'''
- What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?
'''
top_supplier = '''
SELECT ProductName, SupplierId, UnitPrice, CompanyName
FROM Product
JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
'''
curs.execute(top_supplier)


'''
- What is the largest category (by number of unique products in it)?
'''

category = '''
SELECT CategoryId, ProductName, COUNT (DISTINCT CategoryId) as total
FROM Product
'''
curs.execute(category)