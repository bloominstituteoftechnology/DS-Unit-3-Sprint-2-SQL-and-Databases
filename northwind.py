import sqlite3

'''exploration of the northwind dataset in sqlite'''


'''import northwind and make cursor'''
northwind = sqlite3.connect('northwind_small.py')
cursor = northwind.cursor()


'''what are the ten most expensive items per unit price?'''
problem1 = """SELECT ProductName FROM PRODUCT
                  ORDER BY UnitPrice DESC
                  LIMIT 10;"""
print(cursor.execute(problem1).fetchall())


'''What is the average hiring age?'''
problem2 = """SELECT AVG(strftime('%Y', HireDate) - strftime('%Y', BirthDate))
                  FROM Employee;"""
print(cursor.execute(problem2).fetchall()


'''what are the ten most expensive items per unit price BY supplier? '''
problem3 = """SELECT ProductName, CompanyName
                  FROM Product, Supplier
                  WHERE Product.SupplierId = Supplier.Id
                  ORDER BY UnitPrice DESC
                  LIMIT 10;"""
print(cursor.execute(problem3).fetchall())


'''what is the largest category by num of unique products?'''
problem4 = """SELECT COUNT(*)
                  FROM Category, Product
                  WHERE Category.Id = Product.CategoryId
                  GROUP BY CategoryName
                  LIMIT 1;"""
print(cursor.execute(problem4).fetchall())
