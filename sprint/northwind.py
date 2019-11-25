# Importing the SQLite.

import sqlite3

# Creating the connection to the database and the cursor to manipulate it.

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

"""## **Questions to Part 2**

- What are the ten most expensive items (per unit price) in the database?
- What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)
- (*Stretch*) How does the average age of employee at hire vary by city?
"""

# Answer to Question 1.

queryQ1 = """
SELECT ProductName, UnitPrice
FROM Product p
ORDER BY UnitPrice DESC
LIMIT 10
"""
answerQ1 = curs.execute(queryQ1).fetchall()

print('These are the ten most expensive items in this DB.\n')
answerQ1

# Answer to Question 2a.
# I was not sure what was meant by this question.
# This answer calculates avg age of ALL employees at hire date.

queryQ2a = """
SELECT AVG((HireDate - BirthDate)) AS AvgAge
FROM Employee e
"""
answerQ2a = curs.execute(queryQ2a).fetchall()

print(f'Average age at the time of hire is {round(answerQ2a[0][0], 2)}')

# Answer to Question 2b.
# I was not sure what was meant by this question.
# This answer calculates avg age of EACH employees at hire date.

queryQ2b = """
SELECT FirstName, LastName, (HireDate - BirthDate) AS AvgAge
FROM Employee e
"""
answerQ2b = curs.execute(queryQ2b).fetchall()

print('This was age of each employ at the time of hire.\n')
answerQ2b

# Answer to Question 3.

queryQ3 = """
SELECT City, AVG((HireDate - BirthDate)) AS AvgAge
FROM Employee e
GROUP BY City
"""
answerQ3 = curs.execute(queryQ3).fetchall()

print('This is average age per city at the time of hire.\n')
answerQ3

"""## **Questions to Part 3**

- What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?
- What is the largest category (by number of unique products in it)?
- (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
  (not name, region, or other fields) as the unique identifier for territories.
"""

# Answer to Question 4.

queryQ4 = """
SELECT p.ProductName, p.UnitPrice, s.CompanyName
FROM Product p
JOIN Supplier s
ON p.SupplierId = s.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""
answerQ4 = curs.execute(queryQ4).fetchall()

print('Ten most expensive items in this DB and their suppliers.\n')
answerQ4

# Answer to Question 5.

queryQ5 = """
SELECT c.CategoryName, COUNT(*) AS unique_prod
FROM Category c
JOIN Product p
ON c.Id = p.CategoryId
GROUP BY c.CategoryName
ORDER BY unique_prod DESC
"""
answerQ5 = curs.execute(queryQ5).fetchall()

print(f'Largest category of {answerQ5[0][0]} has {answerQ5[0][1]}' +
      ' products in it.')

# Answer to Question 6.

queryQ6 = """
SELECT e.FirstName, e.LastName, COUNT(et.TerritoryId) AS total_territory
FROM Employee e
JOIN EmployeeTerritory et
ON e.Id = et.EmployeeId
GROUP BY e.LastName
ORDER BY total_territory DESC
"""
answerQ6 = curs.execute(queryQ6).fetchall()

print(f'Employee with most ({answerQ6[0][2]}) territories is' +
      f' {answerQ6[0][0]} {answerQ6[0][1]}.')
