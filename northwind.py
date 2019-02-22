import sqlite3

connection = sqlite3.connect('northwind_small.sqlite3')
cursor = connection.cursor()


def northwind_queries():
    """
    returns multiple queries on northwind_small sqlite3 database as print statements
    :return: null: functional printing only
    """
    top_ten_unit_price = cursor.execute(
        "SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;"
    ).fetchall()

    print('Top ten products by price:')

    for row in top_ten_unit_price:
        print(row)

    average_age_hired = cursor.execute("SELECT AVG (HireDate - BirthDate) as Average_Age_Hired FROM Employee")

    print('\nAverage age hired', average_age_hired.fetchall()[0][0])

    age_by_city = cursor.execute("""
    SELECT City, AVG (HireDate - BirthDate) as Average_Age_Hired FROM Employee GROUP BY City
    """).fetchall()

    print("\n Average hire age by city:")

    for row in age_by_city:
        print(row)

    top_ten_price_and_supplier = cursor.execute("""
    SELECT ProductName, UnitPrice, CompanyName, Supplier.Id
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id 
    ORDER BY UnitPrice DESC LIMIT 10
    """).fetchall()

    print('\nTop prices of products with supplier name and ID:')
    for row in top_ten_price_and_supplier:
        print(row)

    categories_by_count = cursor.execute("""
    SELECT CategoryName, Count(Category.Id) as calc
    FROM Category, Product
    WHERE Category.Id = Product.CategoryId
    GROUP BY Category.Id 
    ORDER BY calc DESC;
""")

    print('\nCategories by count of unique products in category: ')
    for row in categories_by_count:
        print(row)


northwind_queries()
