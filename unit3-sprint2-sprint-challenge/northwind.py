import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

# Basic question queries
q0 = """
    SELECT *
    FROM Product
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
    """

# Executing basic question queries
curs0 = conn.cursor()

curs0.execute(q0)
prod0 = curs0.fetchall()
print('Ten Most expensive items:')
for x in prod0:
    print(x)
print('\n')

curs0.close()
conn.commit()

# Advanced question queries
q4 = """
    SELECT * 
    FROM Product
    JOIN Supplier ON Product.SupplierID=Supplier.ID
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
    """

# Executing advanced question queries
curs1 = conn.cursor()
curs1.execute(q4)
prod1 = curs1.fetchmany(10)
print('Most Expensive Items')