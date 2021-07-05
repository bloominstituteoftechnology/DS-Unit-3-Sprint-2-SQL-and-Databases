import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# PART 2
query = """
        SELECT ProductName, UnitPrice
        FROM Product
        ORDER BY 2 DESC
        LIMIT 10
        """
result = curs.execute(query)
print('Top ten most expensive\n', result.fetchall())

query = """
        SELECT AVG(HireDate-BirthDate)
        FROM Employee
        """
result = curs.execute(query)
print('AVG employee age on hire\n', result.fetchall())

# PART 3
query = """
        SELECT ProductName, UnitPrice, s.CompanyName
        FROM Product AS p, Supplier AS s
        INNER JOIN Supplier ON p.SupplierID = s.ID
        ORDER BY 2 DESC
        LIMIT 10
        """
result = curs.execute(query)
print('Most expensive and supplier\n', result.fetchall())

query = """
        SELECT c.CategoryName, COUNT(DISTINCT p.ID)
        FROM Category AS c, Product AS p
        INNER JOIN Category ON c.ID = p.CategoryID
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1
        """
result = curs.execute(query)
print('Largest Category by Number of Products\n', result.fetchall())

# Checking relation between employee and employee territory 
# query = """
#         SELECT COUNT(DISTINCT TerritoryID)
#         FROM EmployeeTerritory
#         """
# result = curs.execute(query)
# print(result.fetchall())

# query = """
#         SELECT COUNT(*)
#         FROM EmployeeTerritory
#         """
# result = curs.execute(query)
# print(result.fetchall())
