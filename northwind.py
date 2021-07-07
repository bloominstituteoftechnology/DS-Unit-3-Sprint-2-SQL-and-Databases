import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# PART TWO
query = 'SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
result = curs.execute(query).fetchall()
print('What are the top ten most expensive items (per unit price)?')
for i in range(len(result)):
    print(str(i+1) + '. ' + result[i][0])

# age is usually referred as an int so casting to integer
query = 'SELECT CAST(AVG(HireDate - BirthDate) AS INTEGER) FROM Employee;'
result = curs.execute(query).fetchone()
print('\nWhat is the average age of an employee at the time of their hiring?',
      result[0])

query = 'SELECT (CAST(AVG(HireDate - BirthDate) AS INTEGER)), City \
         FROM Employee GROUP BY City;'
result = curs.execute(query).fetchall()
print('\nHow does the average age of an employee at hire vary by city?')
for item in result:
    print('City:', item[1])
    print('Avg. Age:', item[0], '\n')

# PART THREE
query = 'SELECT Product.ProductName, Supplier.CompanyName \
         FROM Product, Supplier \
         WHERE Product.SupplierId = Supplier.Id \
         ORDER BY UnitPrice DESC LIMIT 10;'
result = curs.execute(query).fetchall()
print('\nWhat are the ten most expensive items (per unit price) and\
 their suppliers?')
for i in range(len(result)):
    print(str(i+1) + '. ' + 'Item:', result[i][0])
    print('Company:', result[i][1])

query = 'SELECT Category.CategoryName FROM Category \
        WHERE Category.Id = \
            (SELECT CategoryID FROM \
                (SELECT Count(*) as prod_count, Product.CategoryId \
                FROM Product GROUP BY Product.CategoryId \
                ORDER BY prod_count DESC LIMIT 1));'
result = curs.execute(query).fetchone()
print('\nWhat is the largest category (by number of unique products in it)?',
      result[0])

query = 'SELECT FirstName, LastName \
         FROM Employee WHERE ID = ( \
            SELECT EmployeeId FROM ( \
                  SELECT COUNT(TerritoryID) AS cnt, EmployeeId \
                  FROM EmployeeTerritory GROUP BY EmployeeID \
                  ORDER BY cnt DESC LIMIT 1));'
result = curs.execute(query).fetchall()
print('\nWho is the employee with the most territories?',
      result[0][0], result[0][1])
