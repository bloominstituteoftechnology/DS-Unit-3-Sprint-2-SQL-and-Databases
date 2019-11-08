import sqlite3

CONN = sqlite3.connect('northwind_small.sqlite3')

def run_queries():
    """Run and printe output from queries for sprint challenge questions."""
    # Part 2 queries (no joins)
    expensive_items = """SELECT ProductName, UnitPrice
            FROM Product
            ORDER BY UnitPrice DESC
            LIMIT 10;
            """

    avg_age = """SELECT AVG(HireDate - BirthDate)
            FROM Employee;
            """

    avg_age_city = """SELECT AVG(HireDate - BirthDate) AS Average_Age,
                City
                FROM Employee
                GROUP BY City
                ORDER BY Average_Age;
                """

    # Part 3 queries (with joins)
    item_and_supplier = """SELECT Product.ProductName,
                Product.UnitPrice, Supplier.CompanyName
                FROM Product
                INNER JOIN Supplier
                ON Product.SupplierId=Supplier.Id
                ORDER BY UnitPrice DESC
                LIMIT 10;
                """
    largest_category = """SELECT Category.CategoryName,
            COUNT(Product.ProductName) AS Num_Products
            FROM Category
            INNER JOIN Product
            on Product.CategoryId=Category.Id
            GROUP BY Category.CategoryName
            ORDER BY Num_Products DESC
            LIMIT 1
            ;
            """
    emp_most_territory = """SELECT Employee.FirstName,
                Employee.LastName,
                COUNT(EmployeeTerritory.TerritoryId)
                FROM Employee
                INNER JOIN EmployeeTerritory
                ON Employee.Id=EmployeeTerritory.EmployeeId
                GROUP BY EmployeeTerritory.EmployeeId
                ORDER BY COUNT(EmployeeTerritory.TerritoryId) DESC
                LIMIT 1;
                """     

    queries = (expensive_items, avg_age, avg_age_city,
                item_and_supplier, largest_category, emp_most_territory)

    curs = CONN.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())

if __name__ == "__main__":
    run_queries()                    