'''parts 2 and 3 of sprint challenge
'''
import sqlite3 as sl


def part2():
    """queries and reports for part two.

     What are the ten most expensive items (per unit price) in the database?
    What is the average age of an employee at the time of their hiring?
    (Hint: a lot of arithmetic works with dates.)
    (Stretch) How does the average age of employee at hire vary by city?
    """
    conn = sl.connect("northwind_small.sqlite3")

    c = conn.cursor()

    c.execute(
        """SELECT ProductName FROM "Product" ORDER BY UnitPrice DESC LIMIT 10""")

    x = c.fetchall()

    c.execute(
        """SELECT (julianday(HireDate)-julianday(BirthDate))*0.0027378507871321013
        FROM "Employee";""")

    y = c.fetchall()

    c.execute("""SELECT
                ((julianday(Employee.HireDate)-julianday(Employee.BirthDate))*0.0027378507871321013),
                City
                FROM Employee""")

    z = c.fetchall()

    reportx = "These are the 10 most expensive items, in descending order:\n" + \
        "\n".join([f'{k}: {v[0]}' for k, v in enumerate(x)])

    def meany(fetched):
        return sum([t[0] for t in fetched]) / len(fetched)

    reporty = f"The mean hiring age is {meany(y):.2f}"

    reportz = '\n'.join(
        [f'In {t[1]} the mean hiring age is {t[0]:.2f}. ' for t in z])
    conn.close()

    return reportx + '\n\n' + reporty + '\n\n' + reportz + '\n--FIN--\n'


print(part2())


def part3():
    """
    What are the ten most expensive items (per unit price)
        in the database and their suppliers?
    What is the largest category (by number of products in it)?
    (Stretch) What are the top five territories (by number of
        employees), and how many employees do they have?"""

    conn = sl.connect("northwind_small.sqlite3")

    c = conn.cursor()

    c.execute("""SELECT Product.ProductName, Supplier.CompanyName
            FROM "Product"
            LEFT JOIN "Supplier" ON Product.SupplierID = SupplierID
            GROUP BY Product.SupplierID
            ORDER BY Product.UnitPrice DESC LIMIT 10""")

    x = c.fetchall()

    c.execute("""SELECT MAX(Category.CategoryName) FROM Product

            JOIN Category ON Product.CategoryID = CategoryID""")

    y = c.fetchall()

    reportx = "Most expensive items and suppliers, descending order: \n" + \
        '\n'.join([f'{k}: {t[0]}, supplied by {t[1]}' for k, t in enumerate(x)])

    reporty = f"The largest category is {y[0][0]}"

    conn.close()
    return reportx + '\n\n' + reporty + '\n--FIN--\n'


print(part3())

F = open('northwind_OUTPUT.txt', 'w')
F.write(part2())
F.write(part3())
F.close()
