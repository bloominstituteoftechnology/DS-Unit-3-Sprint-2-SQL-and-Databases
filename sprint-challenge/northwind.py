import sqlite3

#Opening connection
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#What are the ten most expensive items (per unit price) in the database?
curs.execute("""
    SELECT ProductName, UnitPrice 
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
""")
answer = curs.fetchall()
print(f'The ten most expensive items are: \n{answer}\n')

#What is the average age of an employee at the time of their hiring?
curs.execute("""
    SELECT SUM(HireDate - BirthDate) / COUNT(*)
    FROM Employee;
""")
answer = curs.fetchall()
print(f'The average hiring age is {answer}.\n')

#Ten most expensive products and their suppliers
curs.execute("""
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product p
    LEFT JOIN Supplier s
    ON p.ID = s.ID
    ORDER BY UnitPrice DESC
    LIMIT 10;
""")
answer = curs.fetchall()
print(f'The ten most expensive products and their suppliers are: \n{answer}\n')

#What is the largest category by number of unique products?
curs.execute("""
    SELECT CategoryName, COUNT(*) - COUNT(DISTINCT CategoryName) 
    FROM Product p
    LEFT JOIN Category c
    ON p.ID = c.ID
    ORDER BY CategoryName DESC;
""")
answer = curs.fetchall()
print(f'The largest category by unique products is {answer}\n')

# Closing connection and committing
curs.close()
conn.commit()