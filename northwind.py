import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

print('Part 2 Question 1.')
ten_most_expensive_products = curs.execute("""SELECT ProductName, UnitPrice FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10""").fetchall()

for product in ten_most_expensive_products:
    print('%s costs %s' % (product[0], product[1]))

print('')
print('')
print('Part 2 Question 2.')
avg_hire_age = curs.execute('SELECT AVG(HireDate - BirthDate) FROM Employee').fetchone()[0]
print('the average age at time of hire is %.2f' % avg_hire_age)
print('')
print('')
print('Part 2 Question 3.')
avg_hire_by_city_query = """SELECT AVG(HireDate - BirthDate) FROM Employee
                            GROUP BY City"""

avg_hires_by_city = curs.execute(avg_hire_by_city_query).fetchall()
for avg_hire in avg_hires_by_city:
    print('average hire age in city: %s' % avg_hire[0])
print('')
print('')

# part 3

products_with_suppliers = curs.execute("""SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product, Supplier
    WHERE Product.SupplierID = Supplier.ID
    ORDER BY UnitPrice DESC
    LIMIT 10""").fetchall()
print('Part 3 Question 1.')
for obj in products_with_suppliers:
    print('product name: %s' % obj[0])
    print('product unit price: %s' % obj[1])
    print('suppliers name: %s' % obj[2])
    print('')
print('')
category_sizes_query = """SELECT Category.CategoryName, COUNT(DISTINCT(Product.ProductName)) AS unique_counts
                          FROM Product, Category
                          WHERE Product.CategoryID = Category.ID
                          GROUP BY Category.CategoryName
                          ORDER BY unique_counts DESC"""
unique_prods_by_category = curs.execute(category_sizes_query).fetchall()
print('Part 3 Question 2.')
for obj in unique_prods_by_category:
    print('Category: %s' % obj[0])
    print('Unique Products: %s ' % obj[1])
    print('')
print('')

print('Part 3 Question 3.')
get_employee_size_query = """SELECT EmployeeTerritory.EmployeeID, COUNT(DISTINCT(EmployeeTerritory.TerritoryID))
                          FROM EmployeeTerritory
                          GROUP BY EmployeeTerritory.EmployeeID
                          ORDER BY COUNT(DISTINCT(EmployeeTerritory.TerritoryID)) DESC
                          LIMIT 1
                          """

emp_name = curs.execute("""SELECT FirstName, LastName FROM Employee WHERE ID = 7""").fetchone()

print('The employee with the most unique territories is %s %s' % (emp_name[0], emp_name[1]))
print('%s has %s unique territories' % (emp_name[0], curs.execute(get_employee_size_query).fetchone()[1]))
