import sqlite3
import pandas as pd

conn = sqlite3.connect('northwind_small.sqlite3')

c = conn.cursor()

##### Expensive Items #####
query = '''
        SELECT
            ID,
            ProductName,
            UnitPrice
        FROM
            Product
        ORDER BY
            UnitPrice
        DESC
        LIMIT
            10
        '''
c.execute(query)
expensive = pd.DataFrame(c.fetchall(),columns=['ID','Product Name','Unit Price'])
print(expensive.head(10),'\n')

##### AVG AGE #####
query = '''
        SELECT cast(strftime('%Y.%m%d', HireDate) - strftime('%Y.%m%d', BirthDate) as int) FROM Employee
        '''
c.execute(query)
print(c.fetchall(),'\n')

##### Most Expensive Items And Suppliers #####
query = '''
            SELECT
                Product.Id,
                Product.ProductName,
                Product.UnitPrice as price,
                Supplier.Id as sid,
                Supplier.CompanyName
            FROM
                Product
            LEFT JOIN
                Supplier
            ON
                Product.SupplierId = sid
            ORDER BY
                price DESC
            LIMIT 10
        '''

c.execute(query)
products_suppliers = pd.DataFrame(c.fetchall(),columns=['Product ID','Product Name','Unit Price','Supplier ID','Company Name'])
print(products_suppliers.head(10),'\n')


##### Largest Category #####
query = '''
        SELECT
            Category.CategoryName,
            COUNT(Product.ProductName) as amount
        FROM
            Category
        LEFT JOIN
            Product
        ON
            Category.Id = Product.CategoryId
        GROUP BY
            Category.CategoryName
        ORDER BY 
            amount DESC
        '''

c.execute(query)
large_cat = pd.DataFrame(c.fetchall(),columns=['Category Name','Amount'])
print(large_cat.head(10))

conn.close()