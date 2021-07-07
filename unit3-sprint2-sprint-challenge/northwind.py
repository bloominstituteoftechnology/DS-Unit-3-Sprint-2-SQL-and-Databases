import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

print('Basic Questions:\n')
# Basic question queries
q0 = """
    SELECT Product.ID, Product.ProductName, Product.UnitPrice
    FROM Product
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
    """
q1 = """
    SELECT AVG(DATE(HireDate)) - AVG(DATE(BirthDate))
    FROM Employee
    """

# Executing basic question queries
curs0 = conn.cursor()

curs0.execute(q0)
prod0 = curs0.fetchall()
print('Ten Most expensive items:')
for x in prod0:
    print(x)

curs0.execute(q1)
print('Average age at Hire:'+str(curs0.fetchone()[0])[:2])

curs0.close()
conn.commit()

print('\n\nAdvanced Questions:\n')
# Advanced question queries
q4 = """
    SELECT Product.ID, Product.ProductName, Product.UnitPrice,Supplier.CompanyName
    FROM Product
    JOIN Supplier ON Product.SupplierID=Supplier.ID
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
    """

q5 = """
    SELECT MAX(a), catName, descrip
    FROM (
        SELECT COUNT(DISTINCT(Product.Id)) AS a,
                Category.CategoryName AS catName,
                Category.Description AS descrip
        FROM Product
        JOIN Category ON Product.CategoryId=Category.ID
        GROUP BY CategoryId
        );
    """
# Executing advanced question queries
curs1 = conn.cursor()

curs1.execute(q4)
prod1 = curs1.fetchmany(10)
print('Most Expensive Items with Company Name:')
for x in prod1:
    print(x)
print('\n')

curs1.execute(q5)
cat = curs1.fetchone()
out = """Largest Category: {},
        Category Size: {},
        Category Description: {}
    """.format(cat[1], cat[0], cat[2])
print(out)