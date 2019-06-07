import sqlite3


conn = sqlite3.Connection('northwind_small.sqlite3')
curs = conn.cursor()

def fetch(query: str) -> None:
  '''
  Query database with the query parameter
  and print the result, returning None.

  Parameters:
  query (str): a valid `sqlite3` select statement

  Returns:
  None
  '''
  try:
    result = curs.execute(query)
  except ValueError as err:
    print('Invalid query. Exiting.', err)
  else:
    print(result.fetchall())
    return None

### PART 2 ###
# List available tables
fetch('''SELECT name
         FROM sqlite_master
         WHERE type='table'
         ORDER BY name;''')


# List columns in Customer table
fetch('SELECT sql FROM sqlite_master WHERE name="Customer";')


# What are the ten most expensive items (per unit price) in the database?
query = '''SELECT DISTINCT ProductName
           FROM Product
           ORDER BY UnitPrice DESC
           LIMIT 10;'''
fetch(query)


# What is the average age of an employee at the time of their hiring?
query = '''SELECT AVG(DATE(HireDate) - DATE(BirthDate))
           FROM Employee;
           '''
fetch(query)


# (Stretch) How does the average age of employee at hire vary by city?
query = '''SELECT City, AVG(DATE(HireDate) - DATE(BirthDate))
           FROM Employee
           GROUP BY City;'''
fetch(query)


### PART 3 ###
# What are the ten most expensive items (per unit price) in the database and their suppliers?
query = '''SELECT DISTINCT ProductName, CompanyName
           FROM Product
           JOIN Supplier
           ON Product.ID = Supplier.ID
           ORDER BY Product.UnitPrice DESC
           LIMIT 10;'''
fetch(query)


# What is the largest category (by number of unique products in it)?
query = '''SELECT CategoryName, COUNT(Product.CategoryID) as category_count
           FROM Category
           JOIN Product
           ON Product.CategoryID = Category.ID
           GROUP BY Product.CategoryID
           ORDER BY category_count DESC
           LIMIT 1;'''
fetch(query)


# (Stretch) Who's the employee with the most territories? 
# Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
query = '''SELECT FirstName || ' ' || LastName, COUNT(TerritoryId) AS territory_count
           FROM EmployeeTerritory
           JOIN Employee
           ON EmployeeTerritory.EmployeeId = Employee.ID
           GROUP BY EmployeeId
           ORDER BY territory_count DESC
           LIMIT 1;'''
fetch(query)