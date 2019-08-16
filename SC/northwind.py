import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


# GET THE TOP 10 MOST EXPENSIVE ITEMS
query = '''
    SELECT UnitPrice, ProductName FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

curs.execute(query)
prices = curs.fetchall()
count = 1
print ('The ten most expensive items')
for price in prices:
    print(f'{count}. {price[1]} costs ${price[0]}')
    count += 1


# WHAT IS THE AVERAGE AGE OF THE EMPLOYEES AT HIRE
query = '''
    SELECT BirthDate, HireDate FROM Employee
'''
curs.execute(query)
employees = curs.fetchall()
employee_ages = []
for emp in employees:
    employee_ages.append(int((emp[1].split('-'))[0]) - int((emp[0].split('-'))[0]))

age_mean = sum(employee_ages) / len(employee_ages)
print(f'\nThe average of of an employee at hire is {age_mean}')


# TEN MOST EXPENSIVE ITEMS WITH THEIR SUPPLIERS
curs = conn.cursor()

query = '''
    SELECT ProductName, UnitPrice, CompanyName AS Supplier FROM Product
    INNER JOIN Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY  Product.UnitPrice DESC
    LIMIT 10;
'''

curs.execute(query)
products = curs.fetchall()
print('\nTen most expensive items with supplier')
count = 1
for product in products:
    print(f'{count}. {product[0]} costs ${product[1]}. The supplier is {product[2]}')
    count += 1


# LARGEST CATEGORY BY UNIQUE PRODUCTS
curs = conn.cursor()
query = '''
SELECT CategoryName, COUNT(DISTINCT ProductName) AS unique_products
FROM Product
INNER JOIN Category
WHERE Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY unique_products DESC;
'''

curs.execute(query)
largest = curs.fetchone()
print(f'{largest[0]} is the largest category with {largest[1]} unique items')

curs.close()
conn.commit()