import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
#query for 10 most expensive items
print('The top ten most expensive products are:')
for row in curs.execute("""SELECT ProductName, UnitPrice FROM Product 
                ORDER BY UnitPrice DESC
                LIMIT 10
""").fetchall():
                    print('name : ',row[0], '-------price $',row[1])
print('The average age of employee at time of hire is',
      curs.execute("""SELECT ROUND(AVG(HireDate-BirthDate),2) FROM Employee
                
        """).fetchall()[0][0],'years old')
#stretch 
print('here is a table displaying average age at hire grouped by city')
for row in curs.execute("""SELECT City,AVG(HireDate-BirthDate) as age FROM Employee
                      GROUP BY CITY
                      ORDER BY AGE DESC
                
        """).fetchall():
                        print('City : ',row[0], '-------average age ',row[1],' years old')
print('The top ten most expensive products and their suppliers are:')
for row in curs.execute("""SELECT ProductName, UnitPrice, CompanyName 
                FROM Product JOIN Supplier
                ON Product.supplierID = Supplier.ID
                ORDER BY UnitPrice DESC
                LIMIT 10
""").fetchall():
    print('Product :',row[0],' -- Price $:',row[1],' -- Supplier :',row[2])
print('the largest category by number of unique products in it is:')
print(curs.execute("""SELECT Description, Count(DISTINCT(Product.ID)) as ct
                FROM Product JOIN Category
                ON Product.CategoryId = Category.ID
                GROUP BY Description
                ORDER BY ct DESC
                LIMIT 1
                
""").fetchall()[0])
print('the employee with the most territories is :')
for row in (curs.execute("""SELECT Employee.FirstName, Employee.LastName,
                Count(DISTINCT(TerritoryId)) as counter 
                FROM Employee JOIN EmployeeTerritory
                ON Employee.ID = EmployeeTerritory.EmployeeID
                GROUP BY Employee.ID, Employee.FirstName, Employee.LastName
                ORDER BY counter DESC
                LIMIT 1
                
""").fetchall()):
    print('is ',row[0],row[1],'with',row[2],'territories')
