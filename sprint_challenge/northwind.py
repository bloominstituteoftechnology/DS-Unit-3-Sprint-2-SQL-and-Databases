import sqlite3

conn = sqlite3.connect("/Users/mattkirby/Desktop/northwind_small.sqlite3")
curs = conn.cursor()


# 1. What are the ten most expensive items (per unit price) in the database?

expensive_query = """SELECT UnitPrice
                     FROM Product
                     ORDER BY UnitPrice DESC
                     LIMIT 10;"""

expensive_result = curs.execute(expensive_query)

print('1. ')
print(expensive_result.fetchall())
print('\n')


# 2. What is the average age of an employee at the time of their hiring?
#    (Hint: a lot of arithmetic works with dates.)

age_query = """SELECT AVG(HireDate - BirthDate)
               FROM Employee;"""

age_result = curs.execute(age_query)

print('2. ')
print(age_result.fetchall())
print('\n')


# 3. What is the average age of an employee at the time of their hiring?
#    (Hint: a lot of arithmetic works with dates.)

#age_query = """SELECT AVG(BirthDate - HireDate)
#               FROM Employee;"""

#age_result = curs.execute(age_query)

#print('3. ')
#print(age_result.fetchall())
#print('\n')


# 4. What are the ten most expensive items
#    (per unit price) in the database and their suppliers?

suppliers_query = """SELECT UnitPrice, CompanyName
                     FROM Product
                     LEFT OUTER JOIN Supplier
			         ON Supplier.ID = Product.SupplierID
                     ORDER BY UnitPrice DESC
                     LIMIT 10;"""

suppliers_result = curs.execute(suppliers_query)

print('4. ')
print(suppliers_result.fetchall())
print('\n')


# 5. What is the largest category (by number of unique products in it)?

category_query = """SELECT CategoryName, COUNT(CategoryId)
                    FROM Product
                    LEFT OUTER JOIN Category
					ON Category.ID = Product.CategoryId
					ORDER BY COUNT(CategoryId) DESC;"""

category_result = curs.execute(category_query)

print('5. ')
print(category_result.fetchall())
print('\n')

"""
1.
[(263.5,), (123.79,), (97,), (81,), (62.5,), (55,), (53,), (49.3,),
 (46,), (45.6,)]


2.
[(37.22222222222222,)]


4. 
[(263.5, 'Aux joyeux ecclésiastiques'),
 (123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
  (97, 'Tokyo Traders'), (81, 'Specialty Biscuits, Ltd.'),
   (62.5, 'Pavlova, Ltd.'), (55, 'Gai pâturage'), (53, "G'day, Mate"),
    (49.3, "Forêts d'érables"), (46, 'Leka Trading'),
     (45.6, 'Plutzer Lebensmittelgroßmärkte AG')]


5.
[('Beverages', 77)]
"""
