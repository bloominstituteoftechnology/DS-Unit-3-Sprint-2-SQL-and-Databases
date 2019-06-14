import sqlite3
connection = sqlite3.connect("northwind_small.sqlite3") 
crsr = connection.cursor() 
crsr.execute("SELECT UNITPRICE FROM Product LIMIT 10;")
ans= crsr.fetchall()  
for i in ans: 
    print(i)
crsr.execute("select 2019 - AVG(BirthDate) from Employee ")
crsr.execute("SELECT UNITPRICE, CompanyName FROM  Product LEFT JOIN Supplier ON PRODUCT.ID  = SUPPLIER.ID LIMIT 10")
ans= crsr.fetchall()  
for i in ans: 
    print(i)
crsr.execute(' SELECT  CategoryName, ProductName, UNITPRICE AS  NUM3 FROM Category LEFT JOIN PRODUCT ON CATEGORY.Id = PRODUCT.CategoryId ORDER BY UnitPrice DESC')
ans= crsr.fetchall()  
for i in ans: 
    print(i) 
