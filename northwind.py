# imports
import sqlite3

# connect to sqlite database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()

curs.execute("SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;").fetchall()

'''
Most expensive items
[('Côte de Blaye',), ('Thüringer Rostbratwurst',), ('Mishi Kobe Niku',),
("Sir Rodney's Marmalade",), ('Carnarvon Tigers',), ('Raclette Courdavault',),
Manjimup Dried Apples',), ('Tarte au sucre',), ('Ipoh Coffee',),
('Rössle Sauerkraut',)]
'''


average_age_query = '''
SELECT avg(diff)
    FROM
    (
    SELECT strftime('%Y', HireDate) - strftime('%Y', BirthDate) as diff
    FROM Employee);
    '''

curs.execute(average_age_query)

'''[(37.22222222222222,)]'''

part_3_query = '''
SELECT ProductName, CompanyName
	FROM
	(
	SELECT Product.ProductName, Supplier.CompanyName
	FROM Product
	JOIN Supplier
	WHERE Product.SupplierId = Supplier.Id
	ORDER BY UnitPrice DESC
    LIMIT 10
	);
	'''

curs.execute(part_3_query)

'''Most expensive items and their suppliers
[('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
('Thüringer Rostbratwurst',
'Plutzer Lebensmittelgroßmärkte AG'),
('Mishi Kobe Niku', 'Tokyo Traders'),
("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
('Carnarvon Tigers', 'Pavlova, Ltd.'),
('Raclette Courdavault', 'Gai pâturage'),
('Manjimup Dried Apples', "G'day, Mate"),
('Tarte au sucre', "Forêts d'érables"),
('Ipoh Coffee', 'Leka Trading'),
('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]
'''

most_unique_products ='''
SELECT CategoryId, count(*) as cnt
FROM Product
GROUP BY CategoryId
ORDER BY COUNT(distinct ProductName) DESC
LIMIT 1'''

curs.execute(most_unique_products)

'''
[(3, 13)]
'''
