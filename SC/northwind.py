'''
This module solves part 2 of the sprint challenge:
working with the Northwind database.
'''
import sqlite3


def answer_query(query, conn, curs, head="Answer:"):
    """
    This function prints the value of a query from a database.
    """
    results = conn.execute(query)
    results = results.fetchall()
    print(head)
    for item in results:
        print(item)
    print("\n")


conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# PART 2:
print("PART 2:")

most_expensive_query = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
answer_query(most_expensive_query, conn, curs,
             "Most expensive items:")

age_employee_query = """
SELECT(AVG(AGE))
FROM(
SELECT (JULIANDAY(HireDate) - JULIANDAY(BirthDate))/365 as age
FROM Employee
)
"""
answer_query(age_employee_query, conn, curs,
             "Avg. age on hire:")

# STRETCH

print("STRETCH: ")

avg_age_city_query = """
SELECT AVG(AGE), City
FROM(
SELECT (JULIANDAY(HireDate) - JULIANDAY(BirthDate))/365 as age, City
FROM Employee
)
GROUP BY City
"""
answer_query(avg_age_city_query, conn, curs,
             "Avg. age on hire by city:")

# PART 3:
print("PART 3:")
most_expensive_supplier_query = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
LEFT JOIN Supplier ON
Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""

answer_query(most_expensive_supplier_query, conn, curs,
             "Most expensive items and their suppliers:")

largest_category_query = """
SELECT CategoryName, MAX(counted) FROM (
SELECT CategoryName, COUNT(DISTINCT Product.id) AS counted
FROM Product
LEFT JOIN Category ON
Product.CategoryId = Category.Id
GROUP BY CategoryName
)
"""
answer_query(largest_category_query, conn, curs,
             "Largest category:")

# STRETCH

print("STRETCH: ")

most_territories_query = """
SELECT FirstName, LastName, MAX(counted) FROM (
SELECT FirstName, LastName, COUNT(DISTINCT TerritoryId) AS counted
FROM Employee
LEFT JOIN EmployeeTerritory ON
Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY EmployeeId
)"""
answer_query(most_territories_query, conn, curs,
             "The employee with the most territories is: ")
