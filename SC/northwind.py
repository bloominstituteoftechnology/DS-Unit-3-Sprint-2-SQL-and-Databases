"""
Part 2 - The Northwind Database
AND
Part 3 - Sailing the Northwind Seas
"""

# Import helper module
import sqlite3_helper as sql3

# Create connection to `northwind.sqlite3` database
conn = sql3.create_connection('northwind_small.sqlite3', verbose=True)

# Use context manager to manage connection to the database
with conn:
    print('-'*80)
    print('Part 2 - The Northwind Database')
    print('-'*80)
    print()
    #########################################################################
    # What are the ten most expensive items (per unit price) in the database?
    #########################################################################
    most_expensive_items_query = """SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
    print('What are the ten most expensive items (per unit price) in the database?')
    results = sql3.select_query(conn, most_expensive_items_query, verbose=True)
    print('-'*80)
    print()
    #########################################################################
    # What is the average age of an employee at the time of their hiring?
    #########################################################################
    print('What is the average age of an employee at the time of their hiring?')
    avg_age_employee_at_hiring_query = """SELECT ROUND(AVG(HireDate-BirthDate), 2) as `Average Age of Employee at Hire` 
                                      FROM Employee;"""
    results = sql3.select_query(
        conn, avg_age_employee_at_hiring_query, verbose=True)
    print('-'*80)
    print()
    #########################################################################
    # (Stretch) How does the average age of employee at hire vary by city?
    #########################################################################
    print('(Stretch) How does the average age of employee at hire vary by city?')
    avg_age_employee_at_hire_vary_by_city_query = """SELECT ROUND(AVG(HireDate-BirthDate), 2) as `Average Age of Employee at Hire`, City
    FROM Employee
    GROUP BY City;"""
    results = sql3.select_query(
        conn, avg_age_employee_at_hire_vary_by_city_query, verbose=True)
    print('-'*80)

    print('Part 3 - Sailing the Northwind Seas')
    print('-'*80)
    print()

    #########################################################################
    # What are the ten most expensive items (per unit price) in the database
    # and their suppliers?
    #########################################################################
    print('What are the ten most expensive items (per unit price) in the database and their suppliers?')
    most_expensive_items_supplier_query = """SELECT ProductName, UnitPrice, CompanyName
    FROM Product
    JOIN Supplier 
        ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;"""
    results = sql3.select_query(
        conn, most_expensive_items_supplier_query, verbose=True)
    print('-'*80)
    print()

    #########################################################################
    # What is the largest category (by number of unique products in it)?
    #########################################################################
    print('What is the largest category (by number of unique products in it)?')
    largest_category_query = """SELECT CategoryName, COUNT(DISTINCT ProductName) AS Count
    FROM Category
    JOIN Product 
        ON Category.Id = Product.CategoryId
    GROUP BY CategoryName
    ORDER BY Count DESC
    LIMIT 1;"""
    results = sql3.select_query(conn, largest_category_query, verbose=True)
    print('-'*80)
    print()

    #########################################################################
    # (Stretch) Who's the employee with the most territories?
    #########################################################################
    print("(Stretch) Who's the employee with the most territories?")
    most_territories_query = """SELECT E.FirstName, E.LastName, COUNT(ET.TerritoryId) AS TerritoryCount 
    FROM Employee AS E
    JOIN EmployeeTerritory AS ET 
        ON E.Id = ET.EmployeeId
    GROUP BY E.Id
    ORDER BY TerritoryCount DESC
    LIMIT 1;"""
    results = sql3.select_query(conn, most_territories_query, verbose=True)
    print('-'*80)
    print()
