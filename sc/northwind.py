conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# view all tables
curs.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;""").fetchall()

# view create table statement for any table
curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()


def highest_prices():
    print(pd.read_sql_query("""SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY 2 DESC
    LIMIT 10;""", conn))


def average_age():
    print(pd.read_sql_query("""SELECT ROUND(AVG(HireDate - BirthDate),2) average_age
    FROM Employee;""", conn))


def employee_age_city():
    print(pd.read_sql_query("""SELECT City, ROUND(AVG(HireDate - BirthDate),2) average_age
        FROM Employee
        GROUP BY City
        ORDER BY 2 DESC;""", conn))


def top_10():
    print(pd.read_sql_query("""SELECT CompanyName, ProductName, UnitPrice FROM Product, Supplier
        WHERE Product.SupplierId = Supplier.Id
        ORDER BY UnitPrice DESC
        LIMIT 10;""", conn))


def largest_category():
    print(pd.read_sql_query("""SELECT CategoryName, COUNT(DISTINCT ProductName) product_count FROM Product, Category
        WHERE Product.CategoryId = Category.Id
        GROUP BY Category.Id
        ORDER BY 2 DESC;""", conn))


def top_5_territories():
    print(pd.read_sql_query("""SELECT TerritoryDescription, COUNT(DISTINCT Employee.Id) employee_count
        FROM EmployeeTerritory, Territory, Employee
        WHERE Territory.Id = EmployeeTerritory.TerritoryId AND Employee.Id = EmployeeTerritory.EmployeeId
        GROUP BY TerritoryDescription
        ORDER BY 2 DESC
        LIMIT 5;""", conn))


def employee_most_territories():
    print(pd.read_sql_query("""SELECT Employee.Id, Employee.LastName, Employee.FirstName,
            COUNT(DISTINCT EmployeeTerritory.TerritoryId) count_territories
            FROM EmployeeTerritory, Employee
            WHERE Employee.Id = EmployeeTerritory.EmployeeId
            GROUP BY Employee.Id
            ORDER BY COUNT(distinct EmployeeTerritory.TerritoryId) DESC
            LIMIT 1;""", conn))











