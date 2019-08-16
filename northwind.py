import sqlite3


def connect_to_db():
    global cursor, conn
    conn = sqlite3.connect('northwind_small.sqlite3')
    cursor = conn.cursor()
    print("Opened database successfully")


def queries_part2():
    print('Ten most expensive items (per unit price) in the database:')
    print(cursor.execute("SELECT ProductName, UnitPrice FROM Product \
    ORDER BY UnitPrice DESC LIMIT 10;").fetchall(), '\n')


    print('The average age of an employee at the time of their hiring')
    print(cursor.execute('SELECT AVG(HireDate-BirthDate) \
    FROM Employee;').fetchall(), '\n')


    print('The average age of employee at hire vary by city')
    print(cursor.execute('SELECT AVG(HireDate-BirthDate) \
    FROM Employee GROUP BY City;').fetchall(), '\n')


def queries_part3():
    print('Ten most expensive items (per unit price) in the database and their suppliers')
    print(cursor.execute('''
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product 
    INNER JOIN Supplier
    ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC LIMIT 10;''').fetchall(), '\n')


    print('The largest category (by number of unique products in it):')
    print(cursor.execute('''SELECT Category.CategoryName
    FROM Category 
    LEFT JOIN Product
    ON Category.Id = Product.CategoryId
    WHERE Product.CategoryId = (SELECT  Product.CategoryId
    FROM PRODUCT
    GROUP BY Product.CategoryId
    ORDER BY Count(*) DESC
    LIMIT 1)
    GROUP BY Product.CategoryId;''').fetchall(), '\n')


def main():
    connect_to_db()
    queries_part2()
    queries_part3()
    conn.close()


if __name__ == "__main__":
    main()