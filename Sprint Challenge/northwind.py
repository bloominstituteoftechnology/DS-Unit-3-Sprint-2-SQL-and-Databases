import sqlite3


def conx_sqlite(db_filename):
    conn = sqlite3.connect(db_filename)
    return conn


def run_queries(cur):
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
        SELECT e.LastName, (e.HireDate - e.Birthdate) as HireAge
        FROM Employee e)
    '''
    print('--- Employee HireAge ---')
    for row in cur.execute(qry):
        print("Average employee hire age is ", round(row[0]))

    # ____ end of queries ___
    return


def main():
    # ____ connect to db ____
    conn = conx_sqlite('northwind_small.sqlite3')
    cur = conn.cursor()

    # _____  Process ______
    run_queries(cur)

    # ___end main ________
    cur.close()
    conn.close()
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
