import sqlite3


con = sqlite3.connect('northwind_small.sqlite3')
curs = con.cursor()

q1 = '''
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;'''
mostExp = curs.execute(q1).fetchall()

q2 = '''
SELECT FirstName, LastName, HireDate - BirthDate
FROM Employee;'''
ages = curs.execute(q2).fetchall()

ageList = []
for i in range(len(ages)):
    ageList.append(ages[i][2])
avgAge = round(sum(ageList)/len(ageList))

q3 = '''
SELECT Product.ProductName, Supplier.CompanyName, Product.UnitPrice
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;'''
mostExpSup = curs.execute(q3).fetchall()

q4 = '''
SELECT Category.CategoryName, COUNT(Category.CategoryName)
FROM Product
INNER JOIN Category
ON Category.Id = Product.CategoryId
GROUP BY Category.CategoryName
ORDER BY COUNT(Category.CategoryName) DESC
LIMIT 1;'''
commonCat = curs.execute(q4).fetchall()

print(f'The average age for an employee at the time of hiring was {avgAge}\n')

print(f'The most common product category was {commonCat[0][0]} which had \
{commonCat[0][1]} unique products\n')

for i in range(len(mostExpSup)):
    print(f'The #{i+1} most expensive product was "{mostExpSup[i][0]}"')
    print(f'It was supplied by "{mostExpSup[i][1]}" ' +
          f'and had a unit price of {mostExpSup[i][2]}\n ')
