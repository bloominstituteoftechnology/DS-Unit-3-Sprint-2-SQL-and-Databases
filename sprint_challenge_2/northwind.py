"""
### Part 2 - The Northwind Database

Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.

![Northwind Entity-Relationship Diagram](./northwind_erd.png)

Above is an entity-relationship diagram - a picture summarizing the schema and
relationships in the database. Note that it was generated using Microsoft
Access, and some of the specific table/field names are different in the
provided data. You can see all the tables available to SQLite as follows:

```python
>>> curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
```

*Warning*: unlike the diagram, the tables in SQLite are singular and not plural
(do not end in `s`). And you can see the schema (`CREATE TABLE` statement)
behind any given table with:
```python
>>> curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";')
                 .fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
"CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
"ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
```

In particular note that the *primary* key is `Id`, and not `CustomerId`. On
other tables (where it is a *foreign* key) it will be `CustomerId`. Also note -
the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that
particular table, but it's a good lesson in the danger of keyword conflicts.

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

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

query_most_expensive = """
    SELECT UnitPrice, ProductName
    FROM product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
curs.execute(query_most_expensive)
most_expensive = curs.fetchall()
i = 0
for most_expensive_i in most_expensive:
    i += 1
    print('The {} most expensive item in the table "product" is: ${}.'
          .format(i, str(most_expensive_i)[1:-1]))

query_avg_age_hire = """
    SELECT round(AVG(HireDate - BirthDate))
    FROM Employee;
    """
curs.execute(query_avg_age_hire)
avg_age_hire = curs.fetchall()[0][0]
print('The average age at the time of hiring is: {}'
      .format(str(avg_age_hire)[:3]))

query_avg_age_hire_city = """
    SELECT round(AVG(HireDate - BirthDate)), City
    FROM Employee
    GROUP BY City;
    """
curs.execute(query_avg_age_hire_city)
avg_age_hire_city = curs.fetchall()
print('The average age at the time of hiring by city is: {}'
      .format(str(avg_age_hire_city)[1:-1]))


# Here I continue to part 3
query_most_expensive_supplier = """
    SELECT pr.UnitPrice, pr.ProductName, supp.CompanyName
    FROM Product AS pr
    JOIN Supplier AS supp
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
curs.execute(query_most_expensive_supplier)
most_expensive_supplier = curs.fetchall()
i = 0
for most_expensive_supplier_i in most_expensive_supplier:
    i += 1
    print('The {} most expensive item with supplier name is: ${}.'
          .format(i, str(most_expensive_supplier_i)[1:-1]))

query_largest_category = """
    SELECT COUNT(pr.ID) as count_id, pr.CategoryId, cat.CategoryName
    FROM Product AS pr
    JOIN Category AS cat
    ON pr.CategoryId = cat.ID
    GROUP BY pr.CategoryId
    ORDER BY count_id DESC
    LIMIT 1;
    """
curs.execute(query_largest_category)
largest_category = curs.fetchall()[0]
print('The largest category by count, ID, name: {}'
      .format(str(largest_category)[1:-1]))

query_employee_most_region = """
    SELECT ep.Id, COUNT(ter.RegionId) as count_region
    FROM Employee AS ep
    JOIN EmployeeTerritory AS ept
    ON ep.Id = ept.EmployeeId
    JOIN Territory as ter
    ON ept.TerritoryId = ter.ID
    GROUP BY ep.ID
    ORDER BY count_region DESC
    LIMIT 1;
    """
curs.execute(query_employee_most_region)
employee_most_region = curs.fetchall()[0]
print('The employee that controls the most regions is ID, number of region: {}'
      .format(str(employee_most_region)[1:-1]))
