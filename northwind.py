import numpy as np
import pandas as pd
def main():
    import sqlite3
    conn = sqlite3.connect('northwind_small.sqlite3') # Open connection to local DB
    c = conn.cursor() # Reference to cursor
    print(list(c.execute('''SELECT ProductName FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10;''')))
    print(list(c.execute('''SELECT avg(date('now') - BirthDate) FROM Employee;''')))
    print(list(c.execute('''SELECT avg(date('now') - BirthDate) FROM Employee
    GROUP BY City;''')))

    top_10_and_suppliers = pd.read_sql_query('''
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product
    INNER JOIN Supplier ON Supplier.Id = Product.SupplierId
    ORDER BY UnitPrice DESC
    LIMIT 10;
    ''', conn)
    print(top_10_and_suppliers)

    top_category_by_unique_products = pd.read_sql_query('''
    SELECT DISTINCT CategoryName, CategoryId, Count(*) AS 'Unique Products'
    FROM Product
    INNER JOIN Category ON Category.Id = Product.CategoryId
    GROUP BY CategoryId
    ORDER BY 3 DESC
    LIMIT 1;
    ''', conn)
    print(top_category_by_unique_products)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()
