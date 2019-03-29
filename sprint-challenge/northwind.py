import sqlite3

DB = '../db/northwind_small.sqlite3'

northwind = sqlite3.connect(DB)

print("Q:", "What are the ten most expensive items (per unit price) in the database?")
print("A:", northwind.execute("select UnitPrice from Product order by UnitPrice desc limit 10").fetchall())

print("Q:", "What is the average age of an employee at the time of their hiring?")
print("A:", northwind.execute("select avg(HireDate - BirthDate) from Employee").fetchall())

print("Q:", "How does the average age of employee at hire vary by city?")
print("A:", northwind.execute("select avg(HireDate - BirthDate), City from Employee group by City").fetchall())
