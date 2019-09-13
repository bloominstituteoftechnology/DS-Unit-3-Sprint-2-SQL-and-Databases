import sqlite3

conn = sqlite3.connect('sc/northwind_small (1).sqlite3')
curs = conn.cursor()

query = 'SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
curs.execute(query)
data = curs.fetchall()
print('The ten most expensive items are:')
x = 1
for d in data:
    print(f'{x}. {d[0]}')
    x += 1

print()

query = """SELECT AVG(strftime('%Y', HireDate) - strftime('%Y', BirthDate))
            FROM Employee;"""
curs.execute(query)
avg_age = curs.fetchall()
print(f'Average age of employee at date of hire is {avg_age[0][0]:.0f}')

print()

# PART 3
query = """SELECT ProductName FROM Product
            JOIN Supplier
            ON Product.SupplierId = Supplier.Id
            ORDER BY product.UnitPrice DESC
            LIMIT 10;"""
curs.execute(query)
info = curs.fetchall()
print('The ten most expensive items are:')
y = 1
for i in info:
    print(f'{y}. {i[0]}')
    y += 1

print()

query = """SELECT CategoryName, COUNT(DISTINCT ProductName) as cp  FROM Category
            JOIN Product
            ON Category.Id = Product.CategoryId
            GROUP BY Category.CategoryName
            ORDER BY cp DESC
            LIMIT 1;"""
curs.execute(query)
top_cat = curs.fetchall()
print('The top category is', top_cat[0][0])
