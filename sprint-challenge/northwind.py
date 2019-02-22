"""Queries to northwind_small SQLite database."""

import sqlite3


if __name__ == "__main__":
    # Create connection to SQLite database and create cursor to database
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()

    # Find top 10 most expensive products in Product table
    expensive_str = """SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;"""
    print("Top 10 most expensive products:")
    for c in curs.execute(expensive_str).fetchall():
        print("\t{}: {}".format(c[0], c[1]))
    print()

    # Find average age of employees when hired from Employee table
    avgage_str = """SELECT AVG(HireDate - BirthDate)
    FROM Employee;"""
    print("Average age at hiring date of employees:")
    print("\t{}".format(curs.execute(avgage_str).fetchone()[0]))
    print()

    # Find average age of employees when hired by city from Employee table
    avgage_bycity_str = """SELECT City, AVG(HireDate - BirthDate)
    FROM Employee
    GROUP BY City;"""
    print("Average age at hiring date of employees by city:")
    for c in curs.execute(avgage_bycity_str).fetchall():
        print("\t{}: {}".format(c[0], c[1]))
    print()
    
    # Find top 10 most expensive products with company name of supplier from
    # Product and Supplier tables
    expensive_supplier_str = """SELECT ProductName, CompanyName, UnitPrice
    FROM Product
    INNER JOIN Supplier ON Supplier.Id = Product.SupplierID
    ORDER BY UnitPrice DESC
    LIMIT 10;"""
    print("Top 10 most expensive products with company name:")
    for c in curs.execute(expensive_supplier_str).fetchall():
        print("\t{} [{}]: {}".format(c[0], c[1], c[2]))
    print()

    # Find category with largest number of products from Product and Category
    # tables
    category_count_str = """SELECT CategoryName, COUNT(*) AS CatCount
    FROM Product
    INNER JOIN Category ON Category.Id = Product.CategoryID
    GROUP BY CategoryName
    ORDER BY CatCount DESC;"""
    print("Category w/ most products:")
    res = curs.execute(category_count_str).fetchone()
    print("\t{}: {}".format(res[0], res[1]))
    print()

    # Find 5 most populous territories for employees from Employee,
    # EmployeeTerritory, and Territory tables
    employee_terr_str = """SELECT TerritoryID,
        TerritoryDescription,
        COUNT(*) AS EmpCount
    FROM (
        SELECT TerritoryID
        FROM Employee
        INNER JOIN EmployeeTerritory
            ON EmployeeTerritory.EmployeeId = Employee.Id
    ) AS EmpTerrID
    INNER JOIN Territory ON Territory.Id = EmpTerrID.TerritoryID
    GROUP BY TerritoryID
    ORDER BY EmpCount DESC
    LIMIT 5;"""
    print("Top 5 most populous employee territories:")
    for c in curs.execute(employee_terr_str).fetchall():
        print("\t{} [{}]: {}".format(c[0], c[1], c[2]))

    # Close connection
    conn.close()
