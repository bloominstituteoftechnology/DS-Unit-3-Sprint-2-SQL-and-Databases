import sqlite3


def query_database(db):
    '''search database and print output'''
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    # - What are the ten most expensive items (per unit price) in the database?
    query = '''
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    '''
    print("ProductName"," : ","UnitPrice")
    for i in cursor.execute(query).fetchall():
        print(i[0]," : ",i[1])
    print("-"*50)

    # - What is the average age of an employee at the time of their hiring? 
    # (Hint: a lot of arithmetic works with dates.)
    query = '''
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;
    '''
    for i in cursor.execute(query).fetchall():
        print("Average Hiring Age:",i[0])
    print("-"*50)

    # - (*Stretch*) How does the average age of employee at hire vary by city?
    query = '''
    SELECT City, AVG(HireDate - BirthDate)
    FROM Employee
    GROUP BY City
    ;'''
    print('City'," : ",'Average Age')
    for i in cursor.execute(query).fetchall():
        print(i[0]," : ",i[1])
    print("-"*50)

    # - What are the ten most expensive items (per unit price) in the database *and* their suppliers?
    query = '''
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product
    JOIN Supplier ON Product.Supplierid = Supplier.id
    ORDER BY UnitPrice DESC
    LIMIT 10
    ;'''
    print("ProductName"," : ","UnitPrice"," : ","CompanyName")
    for i in cursor.execute(query).fetchall():
        print(i[0]," : ",i[1]," : ",i[2])
    print("-"*50)

    # - What is the largest category (by number of unique products in it)?
    query = '''
    SELECT CategoryName, COUNT(ProductName)
    FROM Product
    JOIN Category ON Product.CategoryID = Category.Id
    GROUP BY CategoryName
    ORDER BY COUNT(ProductName) DESC
    LIMIT 1
    ;'''
    for i in cursor.execute(query).fetchall():
        print(i[0]," : ",i[1])
    print("-"*50)

    # - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId` 
    # (not name, region, or other fields) as the unique identifier for territories.
    query = '''
    SELECT LastName, FirstName, COUNT(DISTINCT(TerritoryId))
    FROM EmployeeTerritory
    JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id
    GROUP BY Employee.Id
    ORDER BY COUNT(DISTINCT(TerritoryId)) DESC
    LIMIT 1
    ;'''
    for i in cursor.execute(query).fetchall():
        print(i[0]," : ",i[1]," : ",i[2])
    print("-"*50)


db = 'northwind_small.sqlite3'
query_database(db)

# OUTPUT
################################ 
# ProductName  :  UnitPrice
# Côte de Blaye  :  263.5
# Thüringer Rostbratwurst  :  123.79
# Mishi Kobe Niku  :  97
# Sir Rodney's Marmalade  :  81
# Carnarvon Tigers  :  62.5
# Raclette Courdavault  :  55
# Manjimup Dried Apples  :  53
# Tarte au sucre  :  49.3
# Ipoh Coffee  :  46
# Rössle Sauerkraut  :  45.6
# --------------------------------------------------
# Average Hiring Age: 37.22222222222222
# --------------------------------------------------
# City  :  Average Age
# Kirkland  :  29.0
# London  :  32.5
# Redmond  :  56.0
# Seattle  :  40.0
# Tacoma  :  40.0
# --------------------------------------------------
# ProductName  :  UnitPrice  :  CompanyName
# Côte de Blaye  :  263.5  :  Aux joyeux ecclésiastiques
# Thüringer Rostbratwurst  :  123.79  :  Plutzer Lebensmittelgroßmärkte AG
# Mishi Kobe Niku  :  97  :  Tokyo Traders
# Sir Rodney's Marmalade  :  81  :  Specialty Biscuits, Ltd.
# Carnarvon Tigers  :  62.5  :  Pavlova, Ltd.
# Raclette Courdavault  :  55  :  Gai pâturage
# Manjimup Dried Apples  :  53  :  G'day, Mate
# Tarte au sucre  :  49.3  :  Forêts d'érables
# Ipoh Coffee  :  46  :  Leka Trading
# Rössle Sauerkraut  :  45.6  :  Plutzer Lebensmittelgroßmärkte AG
# --------------------------------------------------
# Confections  :  13
# --------------------------------------------------
# King  :  Robert  :  10
# --------------------------------------------------