import sqlite3

DB_FILE = 'northwind_small.sqlite3' # database to connect to

def create_connection(db_file):
    """Create a database connection to SQLite specified by db_file"""
    conn = None

    try: 
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
            print ("Error in connection", e)
    
    return conn

def topTenPrice(conn):
    """determine the price of the top ten items in the table"""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT ProductName
        FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 10
        """
    )
    rows = cur.fetchall()
    cur.close()

    return rows

def avgEmpAge(conn):
    """determine the average age of employees upon being hired"""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT AVG (HireDate - BirthDate)
        FROM EMPLOYEE
        """
    )
    rows = cur.fetchall()[0][0]
    cur.close()

    return rows

def topTenSuppliers(conn):
    """determine the price of the top ten items and their suppliers"""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT ProductName, CompanyName
        FROM Product
        JOIN Supplier ON Supplier.Id = Product.SupplierId 
        ORDER BY UnitPrice DESC
        LIMIT 10
        """
    )
    rows = cur.fetchall()
    cur.close()

    return rows

def largestCategory(conn):
    """determine the largest category based on number of products"""
    cur = conn.cursor()
    cur.execute(
        """
        SELECT 
            COUNT(DISTINCT ProductName) as totalproducts,
            CategoryName
        FROM Product
        JOIN Category ON Product.CategoryId = Category.Id
        ORDER BY totalproducts DESC
        LIMIT 1
        """
    )
    rows = cur.fetchall()
    cur.close()

    return rows

def main():
    """Run all queries and print statements"""

    # Establish Connection
    conn = create_connection(DB_FILE)

    # Print top ten products by price
    print('Top ten products are:')
    for p in topTenPrice(conn):
        print(p)

    print()

    # Print Average Employee Age
    print(f'The average age of an employee when hired is {avgEmpAge(conn):.2f}')

    print()

    # Print top ten products by price along with thier suppliers
    print('Top ten products and suppliers are:')
    for p in topTenSuppliers(conn):
        print(p)

    print()

    # Print the largest category by products
    cats = largestCategory(conn)
    print(f'The largest category is {cats[0][1]} with {cats[0][0]} products')

if __name__ == "__main__":
    main()

        """OUTPUT"""
        """
        Top ten products are:
        ('Côte de Blaye',)
        ('Thüringer Rostbratwurst',)
        ('Mishi Kobe Niku',)
        ("Sir Rodney's Marmalade",)
        ('Carnarvon Tigers',)
        ('Raclette Courdavault',)
        ('Manjimup Dried Apples',)
        ('Tarte au sucre',)
        ('Ipoh Coffee',)
        ('Rössle Sauerkraut',)

        The average age of an employee when hired is 37.22

        Top ten products and suppliers are:
        ('Côte de Blaye', 'Aux joyeux ecclésiastiques')
        ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG')
        ('Mishi Kobe Niku', 'Tokyo Traders')
        ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.')
        ('Carnarvon Tigers', 'Pavlova, Ltd.')
        ('Raclette Courdavault', 'Gai pâturage')
        ('Manjimup Dried Apples', "G'day, Mate")
        ('Tarte au sucre', "Forêts d'érables")
        ('Ipoh Coffee', 'Leka Trading')
        ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')

        The largest category is Beverages with 77 products
        """
        