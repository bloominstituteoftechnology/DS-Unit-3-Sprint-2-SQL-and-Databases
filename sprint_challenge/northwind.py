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

age_query = """SELECT AVG(BirthDate - HireDate)
               FROM Employee;"""

age_result = curs.execute(age_query)

print('2. ')
print(age_result.fetchall())
print('\n')
