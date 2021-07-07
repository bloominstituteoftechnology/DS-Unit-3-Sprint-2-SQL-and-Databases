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
    
'''Docstring answersThe top ten most expensive products are:
name :  Côte de Blaye -------price $ 263.5
name :  Thüringer Rostbratwurst -------price $ 123.79
name :  Mishi Kobe Niku -------price $ 97
name :  Sir Rodney's Marmalade -------price $ 81
name :  Carnarvon Tigers -------price $ 62.5
name :  Raclette Courdavault -------price $ 55
name :  Manjimup Dried Apples -------price $ 53
name :  Tarte au sucre -------price $ 49.3
name :  Ipoh Coffee -------price $ 46
name :  Rössle Sauerkraut -------price $ 45.6
The average age of employee at time of hire is 37.22 years old
here is a table displaying average age at hire grouped by city
City :  Redmond -------average age  56.0  years old
City :  Seattle -------average age  40.0  years old
City :  Tacoma -------average age  40.0  years old
City :  London -------average age  32.5  years old
City :  Kirkland -------average age  29.0  years old
The top ten most expensive products and their suppliers are:
Product : Côte de Blaye  -- Price $: 263.5  -- Supplier : Aux joyeux ecclésiastiques
Product : Thüringer Rostbratwurst  -- Price $: 123.79  -- Supplier : Plutzer Lebensmittelgroßmärkte AG
Product : Mishi Kobe Niku  -- Price $: 97  -- Supplier : Tokyo Traders
Product : Sir Rodney's Marmalade  -- Price $: 81  -- Supplier : Specialty Biscuits, Ltd.
Product : Carnarvon Tigers  -- Price $: 62.5  -- Supplier : Pavlova, Ltd.
Product : Raclette Courdavault  -- Price $: 55  -- Supplier : Gai pâturage
Product : Manjimup Dried Apples  -- Price $: 53  -- Supplier : G'day, Mate
Product : Tarte au sucre  -- Price $: 49.3  -- Supplier : Forêts d'érables
Product : Ipoh Coffee  -- Price $: 46  -- Supplier : Leka Trading
Product : Rössle Sauerkraut  -- Price $: 45.6  -- Supplier : Plutzer Lebensmittelgroßmärkte AG
the largest category by number of unique products in it is:
('Desserts, candies, and sweet breads', 13)
the employee with the most territories is :
is  Robert King with 10 territories'''
