import sqlite3

#Opening connection
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#Viewing table names
curs.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    )
answer = curs.fetchall()
print(f'The table names are: \n{answer}\n')

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
print(f'The average age at hiring is {answer}.\n')
