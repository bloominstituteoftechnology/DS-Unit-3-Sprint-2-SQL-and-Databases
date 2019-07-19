import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

def part2Question1():
    """Part 2 Question 1:
    - Côte de Blaye
    - Thüringer Rostbratwurst
    - Mishi Kobe Niku
    - Sir Rodney's Marmalade
    - Carnarvon Tigers
    - Raclette Courdavault
    - Manjimup Dried Apples
    - Tarte au sucre
    - Ipoh Coffee
    - Rössle Sauerkraut"""
    cur.execute("""
        SELECT ProductName, UnitPrice
        FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10;
    """)
    conn.commit()
    print(cur.fetchall(), "\n")

def part2Question2():
    """Part 2 Question 2: 37(.2)"""
    cur.execute("""
        SELECT AVG(BirthDate - HireDate) as yrs_since_hire
        FROM Employee;
    """)
    conn.commit()
    print(cur.fetchall(), "\n")

def part3Question1():
    """Part 3 Question 1:
    - Côte de Blaye, 'Aux joyeux ecclésiastiques', 263.5
    - Thüringer Rostbratwurst, 'Plutzer Lebensmittelgroßmärkte AG', 123.79
    - Mishi Kobe Niku, 'Tokyo Traders', 97
    - Sir Rodney's Marmalade, 'Specialty Biscuits, Ltd.', 81
    - Carnarvon Tigers, 'Pavlova, Ltd.', 62.5
    - Raclette Courdavault, 'Gai pâturage', 55
    - Manjimup Dried Apples, "G'day, Mate", 53
    - Tarte au sucre, "Forêts d'érables", 49.3
    - Ipoh Coffee, 'Leka Trading', 46
    - Rössle Sauerkraut', Plutzer Lebensmittelgroßmärkte AG', 45.6"""
    cur.execute("""
        SELECT Product.ProductName AS 'Product Name', Supplier.CompanyName AS 'Supplier Name', Product.UnitPrice AS 'Price'
        FROM Product
        JOIN Supplier
        ON Product.SupplierId = Supplier.Id
        ORDER BY Product.UnitPrice DESC
        LIMIT 10;
    """)
    conn.commit()
    print(cur.fetchall(), "\n")

def part3Question2():
    """Part 3 Question 2: The 'Confections' category, which has 13 products in it."""
    cur.execute("""
        SELECT Category.CategoryName, COUNT(*) as 'Unique Products'
        FROM Product
        INNER JOIN Category
        ON Product.CategoryId = Category.Id
        GROUP BY Category.Id
        ORDER BY COUNT(*) DESC;
    """)
    print(cur.fetchall(), "\n")

####
print("Part 2 Question 1")
part2Question1()

print("Part 2 Question 2")
part2Question2()

print("Part 3 Question 1")
part3Question1()

print("Part 3 Question 2")
part3Question2()