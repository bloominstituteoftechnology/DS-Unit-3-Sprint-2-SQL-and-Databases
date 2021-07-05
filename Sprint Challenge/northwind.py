"""
The purpose of this program is to query the northwind database
in conjunction with the DS3 Unit-3 Sprint-2 Sprint Challenge.
The instructions are as follows:

############################################################

Answer the following questions (each is from a single table):

- What are the ten most expensive items (per unit price) in the database?
- What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)
- (*Stretch*) How does the average age of employee at hire vary by city?

Your code (to load and query the data) should be saved in `northwind.py`, and
added to the repository. Do your best to answer in purely SQL, but if necessary
use Python/other logic to help.

### Part 3 - Sailing the Northwind Seas

You've answered some basic questions from the Northwind database, looking at
individual tables - now it's time to put things together, and `JOIN`!

Using `sqlite3` in `northwind.py`, answer the following:

- What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?
- What is the largest category (by number of unique products in it)?
- (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
  (not name, region, or other fields) as the unique identifier for territories.
"""
import sqlite3

# Establishing connection to the database and a cursor.
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Setting my queries as global variables so you can read them more easily.

query_1 = ("SELECT ProductName\n"
           "FROM Product\n"
           "ORDER BY UnitPrice DESC\n"
           "LIMIT 10")

query_2 = ("SELECT avg(HireDate - BirthDate)\n"
           "from Employee")

query_3 = ("SELECT avg(HireDate-BirthDate),  City\n"
           "FROM Employee\n"
           "GROUP BY City")

query_4 = ("SELECT ProductName, CompanyName\n"
           "FROM \n"
           "Product, Supplier\n"
           "WHERE\n"
           "Product.SupplierId = Supplier.Id\n"
           "ORDER BY UnitPrice DESC\n"
           "LIMIT 10")

query_5 = ("SELECT CategoryName\n"
           "FROM Product, Category\n"
           "WHERE Product.CategoryId = Category.Id\n"
           "GROUP BY CategoryID\n"
           "ORDER BY COUNT(Categoryid) DESC\n"
           "LIMIT 1")

query_6 = ("SELECT FirstName || \" \" || LastName\n"
           "FROM \n"
           "EmployeeTerritory, Employee, Territory\n"
           "WHERE \n"
           "EmployeeTerritory.EmployeeId = Employee.Id AND\n"
           "EmployeeTerritory.TerritoryId = TerritoryId\n"
           "GROUP BY EmployeeId\n"
           "ORDER BY  COUNT(TerritoryId) DESC\n"
           "LIMIT 1")

print("Question 1: \n",
      "Ten Most Expensive Items:\n",
      curs.execute(query_1).fetchall())

print("Question 2: \n",
      "Average Age of Employee Upon Hiring:",
      curs.execute(query_2).fetchall()[0][0])

print("Question 3: \n",
      "Average Age of Employee by City: \n",
      curs.execute(query_3).fetchall())

print("Question 4: \n",
      "Ten Most Expensive Items and their suppliers \n",
      curs.execute(query_4).fetchall())

print("Question 5: \n",
      "Largest Category:",
      curs.execute(query_5).fetchall()[0][0])

print("Quesiton 6: \n",
      "Employee With the Most Territories:",
      curs.execute(query_6).fetchall()[0][0])

