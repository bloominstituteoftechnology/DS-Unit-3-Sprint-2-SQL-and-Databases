import sqlite3

!wget https://github.com/jonathanmendoza-tx/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/northwind_small.sqlite3?raw=true -O northwind_small.sqlite3

#create connection
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

query_most_expensive = """
	SELECT ProductName
	FROM Product
	ORDER BY UnitPrice DESC
	"""

cur.execute(query_most_expensive)
most_expensive = cur.fetchall()

expensive_products = list(zip(*most_expensive))

print(f'The top 10 most expensive items are: \n {expensive_products[:10]}')

query_avg_age = """
	SELECT AVG(HireDate - BirthDate)
	FROM Employee
	"""

cur.execute(query_avg_age)
avg_age_at_hire = cur.fetchall()

print(f'The average age of a new-hire is {avg_age_at_hire[0][0]}')

query_expensive_suppliers = """
  SELECT p.ProductName, s.ContactName
  FROM Product p
	  INNER JOIN Supplier s 
	  ON p.SupplierId = s.Id
  ORDER BY p.UnitPrice DESC
  """

cur.execute(query_expensive_suppliers)
expensive_products_and_suppliers = cur.fetchall()

print(f'Top ten most expensive products and their suppliers: \n(Product, Supplier)\n{expensive_products_and_suppliers[:10]}')

query_largest_category = """
	SELECT c.CategoryName, COUNT(p.CategoryId) AS total_in_category
	FROM Product p
		INNER JOIN Category c
		ON p.CategoryId = c.Id
	GROUP BY CategoryName 
	ORDER BY total_in_category DESC
	"""

cur.execute(query_largest_category)
category_counts = cur.fetchall()

print(f'The largest category is {category_counts[0][0]}')
