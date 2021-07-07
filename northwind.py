import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()

query1 = 'SELECT ProductName FROM Product \
         ORDER BY UnitPrice DESC LIMIT 10;'
answer1 = cursor.execute(query1).fetchall()
print('The 10 most expensive items are: ', answer1)

query2 = 'SELECT (CAST (AVG (HireDate - BirthDate) \
         AS INTEGER)) FROM Employee;'
answer2 = cursor.execute(query2).fetchone()[0]
print('Average age of employee at hiring is ', answer2, 'years old.')

query3 = 'SELECT (CAST (AVG (HireDate - BirthDate) \
        AS INTEGER)), City FROM Employee \
        GROUP BY City;'
answer3 = cursor.execute(query3).fetchall()
print('Average age difference by City')
print(answer3)

query4 = 'SELECT ProductName, CompanyName \
        FROM Product \
        INNER JOIN Supplier \
            ON Product.SupplierID = Supplier.ID \
        ORDER BY UnitPrice DESC LIMIT 10;'
answer4 = cursor.execute(query4).fetchall()
print('The 10 most expensive items and their supplier are', answer4)

query5 = 'SELECT CategoryName FROM Category \
        WHERE Category.Id = (SELECT CategoryID FROM \
        (SELECT COUNT(*) AS product_count, Product.CategoryId \
        FROM Product \
        GROUP BY Product.CategoryId \
        ORDER BY product_count DESC LIMIT 1));'
answer5 = cursor.execute(query5).fetchone()[0]
print(answer5, 'is the largest category by number of unique products.')

query6 = 'SELECT FirstName, LastName from Employee \
        WHERE Id = (SELECT EmployeeId \
        FROM (SELECT COUNT (TerritoryId) AS territory_count, EmployeeId \
        FROM EmployeeTerritory \
        GROUP BY EmployeeId \
        ORDER BY territory_count DESC LIMIT 1));'
answer6 = cursor.execute(query6).fetchone()
print(answer6[0], answer6[1], 'is the employee with the most territories')

conn.commit()
conn.close()
