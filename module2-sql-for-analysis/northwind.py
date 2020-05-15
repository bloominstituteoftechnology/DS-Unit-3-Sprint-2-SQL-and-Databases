import sqlite3
DATABASE = (r'./northwind_small.sqlite3')
conn = sqlite3.connect(DATABASE)
curs = conn.cursor()
test_query = """
SELECT * 
FROM Employee
"""
test_results = curs.execute(test_query)
test_results1 = curs.fetchall()
#print(test_results1)


query1 = """
SELECT DISTINCT ProductId,
       UnitPrice
FROM OrderDetail
ORDER BY UnitPrice DESC
LIMIT 10
"""

result1 = curs.execute(query1)
results1 = curs.fetchall()
#print(results1)
for row in results1:
    print("The product number",row[0], "has a unitprice of ",row[1])
query2 = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""

result2 = curs.execute(query2)
results2 = curs.fetchall()
#print(results2)
print("The average age of an employee at time of hiring is",results2[0])

query3 = """
SELECT DISTINCT Product.Id,
       Product.ProductName,
       Supplier.CompanyName,
       Supplier.Id as Supplier,
       Product.UnitPrice
FROM Product
LEFT JOIN Supplier ON Supplier.Id = Product.SupplierId
ORDER BY UnitPrice DESC
LIMIT 10
"""
result3 = curs.execute(query3)
results3 = curs.fetchall()
#print(results3)
for row in results3:
    print('The Product', row[1], "has a price of", row[4], 'supplied by',row[2])
query4 = """
SELECT COUNT(Product.CategoryId)as product_count,
       Category.CategoryName
FROM Product
JOIN Category on Product.CategoryId = Category.Id
GROUP BY Product.CategoryId
ORDER BY product_count DESC
LIMIT 1
"""

result4 = curs.execute(query4)
results4 = curs.fetchall()
#print(results4)
print("The largest category in the database is",results4[0][1], "with",results4[0][0], "items in the category.")

#Stretch Who's the employee with the most territories? Use `TerritoryId`

