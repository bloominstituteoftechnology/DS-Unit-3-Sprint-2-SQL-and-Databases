import pandas as pd 
import sqlite3 

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

"What are the ten most expensive items (per unit price) in the database?"
query = """
           SELECT ProductName, UnitPrice
           FROM Product
           ORDER BY UnitPrice DESC
           LIMIT 10;
        """
top_ten = curs.execute(query).fetchall()
df = pd.DataFrame(top_ten, columns = ['product', 'price'])
df = df.set_index('product')
print(df)

"What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)"
query = """
           SELECT AVG(HireDate - BirthDate)
           FROM Employee;
        """
avg_age = curs.execute(query).fetchall()[0][0]
print(f'Average age of employees at the hiring time is {avg_age}')

"How does the average age of employee at hire vary by city?"
query = """
           SELECT 
                 City,
                 AVG(HireDate - BirthDate)
            FROM Employee
            GROUP BY 1
            ORDER BY 2;
        """
age_by_city = curs.execute(query).fetchall()
df = pd.DataFrame(age_by_city, columns = ['city', 'avg_age'])
df = df.set_index('city')
print(df)

"What are the ten most expensive items (per unit price) in the database and their suppliers?"
query = """
           SELECT p.ProductName, s.CompanyName, p.UnitPrice
           FROM Product p
           JOIN Supplier s
           ON s.ID = p.SupplierID
           ORDER BY p.UnitPrice DESC
           LIMIT 10;
        """
top_ten_1 = curs.execute(query).fetchall()
df = pd.DataFrame(top_ten_1, columns = ['product', 'supplier', 'price'])
df = df.set_index('product')
print(df)

"What is the largest category (by number of unique products in it)?"
query = """
           SELECT 
                 c.CategoryName,
                 COUNT(distinct p.ProductName) as unique_products
            FROM Product p
            JOIN Category c
            ON c.ID = p.CategoryID
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 10
        """
unique_products = curs.execute(query).fetchall()
df = pd.DataFrame(unique_products, columns = ['category', 'number'])
df = df.set_index('category')
print(df)
print(f'Largest category is {unique_products[0][0]} with {unique_products[0][1]} products')

"Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories."
query = """
           SELECT 
                 e.FirstName,
                 e.LastName,
                 COUNT(et.TerritoryId) AS total_territory
            FROM Employee e
            JOIN EmployeeTerritory et
            ON e.ID = et.EmployeeID
            GROUP BY 2
            ORDER BY 3 DESC;   
        """
total_territory = curs.execute(query).fetchall()
df = pd.DataFrame(total_territory, columns = ['firstname', 'lastname', 'number'])
df = df.set_index('firstname')
print(df)
print(f'Employee {total_territory[0][0]} {total_territory[0][1]} has the most number of territories, which is {total_territory[0][2]}')         