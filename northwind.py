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