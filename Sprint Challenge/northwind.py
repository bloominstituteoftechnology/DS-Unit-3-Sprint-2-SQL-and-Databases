import sqlite3


def conx_sqlite(db_filename):
    conn = sqlite3.connect(db_filename)
    return conn


def run_queries(cur):
    print('____________NORTHWIND STATUS REPORT ___________________\n')
    # ___ 10 most expensive Products __________________________________________
    qry = '''
    SELECT p.ProductName, p.UnitPrice
    FROM Product p
    ORDER BY p.UnitPrice DESC
    LIMIT 10;
    '''
    print('--- 10 Most Expensive Items ---')
    for row in cur.execute(qry):
        print(row[0], ".......", row[1])

    # ___ Average Employee Hire Age_____________________
    qry = '''
    SELECT Avg(HireAge)
    FROM (
        SELECT e.LastName, (e.HireDate - e.Birthdate) HireAge
        FROM Employee e)
    '''
    print('\n--- Employee HireAge ---')
    for row in cur.execute(qry):
        print("Average employee hire age is", round(row[0]))

    # __ How does the average age of employee at hire vary by city __
    qry = '''
    SELECT e.City,  AVG(e.HireDate-e.Birthdate) HireAge
    FROM Employee e
    GROUP BY e.City
    ORDER BY e.City, HireAge DESC
    '''
    print('\n--- Employee HireAge by City---')
    for row in cur.execute(qry):
        print(row[0], '...', row[1])

    # ___ 10 most expensive Products with Suppliers ___________
    qry = '''
    SELECT p.ProductName, p.UnitPrice, s.CompanyName
    FROM Product p
    JOIN Supplier s
      ON p.Supplierid = s.id
    ORDER BY p.UnitPrice DESC
    LIMIT 10;
    '''
    print('\n--- 10 Most Expensive Items and Supplier ---')
    for row in cur.execute(qry):
        print(row[0], "....", row[1], "...", row[2])

    # ___ Category by Number of Products ___________
    qry = '''
    SELECT c.CategoryName, COUNT(p.ProductName) pCount
    FROM Category c
    JOIN Product p
      ON p.Categoryid = c.id
    GROUP BY c.CategoryName
    ORDER BY pCount DESC
    '''
    print('\n-- 10 Largest Categories by # of Products --')
    for row in cur.execute(qry):
        print(row[0], "....", row[1])
    # __What are the top five territories (by number of employees)__
    qry = '''
    SELECT t.TerritoryDescription, COUNT(e.LastName) eCount
    From EmployeeTerritory et
    JOIN Employee e  ON et.EmployeeId = e.id
    JOIN Territory t ON et.TerritoryId = t.id
    GROUP BY t.TerritoryDescription
    ORDER BY eCount DESC
    LIMIT 5
    '''
    print('\n-- 5 Top Territories by # of employees --')
    for row in cur.execute(qry):
        print(row[0], '...', row[1])

    return


def run_new_queries(cur):
    # ____ end of queries ___
    return


def main():
    # ____ connect to db ____
    conn = conx_sqlite('northwind_small.sqlite3')
    cur = conn.cursor()

    # _____  Process ______
    run_queries(cur)
    run_new_queries(cur)

    # ___end main ________
    cur.close()
    conn.close()
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
