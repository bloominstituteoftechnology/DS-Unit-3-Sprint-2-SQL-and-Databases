import sqlite3

# PART 2

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

ten_priciest_query = ('''
    SELECT UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
    ''')

ten_priciest_print = curs.execute(ten_priciest_query).fetchall()
print(ten_priciest_print)

avg_age_query = ('''
    SELECT AVG(HireDate-BirthDate)
    FROM Employee
    ''')

avg_age_print = curs.execute(avg_age_query).fetchall()
print(avg_age_print)


# PART 3

ten_priciest_join_query = ('''
    SELECT CompanyName, ProductName, UnitPrice
    FROM Product, Supplier
    GROUP BY ProductName
    ORDER BY UnitPrice DESC
    LIMIT 10;
    ''')

ten_priciest_join_print = curs.execute(ten_priciest_join_query).fetchall()
print(ten_priciest_join_print)

largest_category_unique_query = ('''
    SELECT Category.CategoryName, COUNT(Product.CategoryID)
    FROM Product
    INNER JOIN Category
    ON Product.CategoryID=Category.ID
    GROUP BY Category.ID
    ORDER BY COUNT(Product.CategoryID) DESC
    LIMIT 1;
    ''')

largest_category_unique_print = curs.execute(largest_category_unique_query).fetchall()
print(largest_category_unique_print)

curs.close()
conn.commit()