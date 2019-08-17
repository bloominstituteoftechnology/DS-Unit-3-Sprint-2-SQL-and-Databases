import sqlite3


""" 
docstring for answers to non-stretch questions

1.  Côte de Blaye	263.5
    Thüringer Rostbratwurst	123.79
    Mishi Kobe Niku	97
    Sir Rodney's Marmalade	81
    Carnarvon Tigers	62.5
    Raclette Courdavault	55
    Manjimup Dried Apples	53
    Tarte au sucre	49.3
    Ipoh Coffee	46
    Rössle Sauerkraut	45.6

2.  37.2222222222222

3.  263.5	Aux joyeux ecclésiastiques
    123.79	Plutzer Lebensmittelgroßmärkte AG
    97	Tokyo Traders
    81	Specialty Biscuits, Ltd.
    62.5	Pavlova, Ltd.
    55	Gai pâturage
    53	G'day, Mate
    49.3	Forêts d'érables
    46	Leka Trading
    45.6	Plutzer Lebensmittelgroßmärkte AG

4. Confections

"""

# Instantiate connection to database and initialize cursor
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()


# Query for top ten most expensive products
query = """
    SELECT ProductName, UnitPrice
    FROM Product 
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""
curs.execute(query)
print('Top ten most expensive projects:', curs.fetchall())


# Query for average age of employees when hired
query = """
    SELECT AVG(HireDate) - AVG(BirthDate)
    FROM  Employee
"""
curs.execute(query)
print('Average age of employees when hired:', curs.fetchall()[0][0])


# Query for top ten expensive products and their suppliers
query = """
    SELECT UnitPrice, Supplier.CompanyName
    FROM Product
    INNER JOIN Supplier
    ON Product.SupplierID = Supplier.ID
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""
curs.execute(query)
print('Ten most expensive by unit price/supplier:', curs.fetchall())


# Query for the largest category
query = '''
    SELECT MAX(cnt), CategoryName
    FROM (SELECT CategoryName, COUNT(*) as cnt
          FROM Product
          INNER JOIN Category
          ON Product.CategoryID = Category.ID
          GROUP BY CategoryName);
'''
curs.execute(query)
print('Category with the most unique products:', curs.fetchall()[0][1])

curs.close()
conn.commit()
