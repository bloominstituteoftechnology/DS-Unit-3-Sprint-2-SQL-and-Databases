#!/usr/bin/env python3

import sqlite3


def nice_print(sql_table):
    """ used to show information in a slightly more readable fashion"""
    for row in sql_table:
        row_string = map(str,row)
        pretty_row = '\t\t'.join(list(row_string))
        print(pretty_row)

conn = sqlite3.connect('northwind.sqlite3')
curs = conn.cursor()

# Basic Questions
ten_expensive = """
SELECT ProductName, UnitPrice
        from Product
        ORDER BY UnitPrice DESC
        LIMIT 10;
"""
avg_age = """
SELECT ROUND(AVG(HireDate - BirthDate)) as "average hire age"
        from Employee;
"""
avg_age_city = """
SELECT City, ROUND(AVG(HireDate - BirthDate)) as "average hire age by City"
        from Employee
        GROUP BY City;
"""

print("\n\ntop 10 most expensive items")
nice_print(curs.execute(ten_expensive).fetchall())
print("\n\navg. age at hire")
nice_print(curs.execute(avg_age).fetchall())
print("\n\navg. age by city")
nice_print(curs.execute(avg_age_city).fetchall())


# Advanced Questions
ten_expensive_supplier = """
SELECT ProductName, UnitPrice, CompanyName
        from Product JOIN Supplier
			ON Product.SupplierID = Supplier.Id
        ORDER BY UnitPrice DESC
        LIMIT 10;
"""
largest_category = """
SELECT CategoryName, COUNT(ProductName) as "count"
	FROM Product JOIN Category
		ON Product.CategoryId = Category.Id
	GROUP BY CategoryName
	ORDER BY "count" DESC
	LIMIT 1;
"""
give_raise_to_this_employee = """
SELECT FirstName || ' ' ||  LastName as fullname
	FROM Employee JOIN EmployeeTerritory
		ON Employee.Id = EmployeeTerritory.EmployeeId
	GROUP BY fullname
	ORDER BY COUNT( DISTINCT TerritoryId) DESC
	LIMIT 1;
"""

print("\n\nWhat are the 10 most expensive items AND their Supplier?")
nice_print(curs.execute(ten_expensive_supplier).fetchall())
print("\n\nWhat is the largest category (by unique products)")
nice_print(curs.execute(largest_category).fetchall())
print("\n\nWho's the employee with the most territories?")
nice_print(curs.execute(give_raise_to_this_employee).fetchall())

