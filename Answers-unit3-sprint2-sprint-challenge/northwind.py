import sqlite3

def query(x, db="northwind_small.sqlite3"):
    '''
    - This function connects to a database, 
    - establishes a cursor on top of the connection,
    - executes the SQL command = x
    - fetches the results from the SQL command and store it 
    in the variable ANSWER
    - Then commits and close the cursor and connection
    - then returns the result of the query.
    '''
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.close()
    conn.commit()
    return answer

# Part 2 - The Northwind Database

# getting a preview of the table
data_preview = """SELECT * FROM product limit 10"""

query(data_preview)

# table pragma

pragma = """PRAGMA table_info (product);"""
query(pragma)

# What are the ten most expensive items (per unit price) in the database?

expensive = """SELECT ProductName, UnitPrice 
                FROM product
                ORDER BY UnitPrice DESC
                LIMIT 10;
                """
query(expensive)

# What is the average age of an employee at the time of their hiring?

# table preview
pragma = """PRAGMA table_info (employee);"""
query(pragma)

avg_age = """SELECT 
          ROUND(AVG(HireDate - BirthDate),1)
          from employee """
query(avg_age)  

# (*Stretch*) How does the average age of employee at hire vary by city?

# idea is to calculate the (average age - the age) for each city. 

avg_age_city = """SELECT City,
          ROUND(AVG(HireDate - BirthDate),1)
          from employee 
          GROUP BY City"""
query(avg_age_city) 

# Part 3 - Sailing the Northwind Seas

#What are the ten most expensive items (per unit price) in the database *and* their suppliers?

query('PRAGMA table_info (supplier);')

expensive_suppliers = """SELECT 
                p.ProductName, 
                p.UnitPrice, 
                s.Id,
                s.CompanyName
                FROM product as p, 
                supplier as s
                WHERE s.Id = p.SupplierId
                ORDER BY UnitPrice DESC
                LIMIT 10;
                """
query(expensive_suppliers)

# What is the largest category (by number of unique products in it). 

#Basically, which category has the most unique products in it. 

query('PRAGMA table_info (category);') #still no clue what question is asking

category_product = """SELECT 
                c.CategoryName,
                COUNT(DISTINCT p.ProductName)
                FROM product as p
                INNER JOIN category as c
                ON p.CategoryId = c.Id
                GROUP BY c.CategoryName
                ORDER BY COUNT(DISTINCT p.ProductName) DESC
                LIMIT 1;
                    """
query(category_product)


# (*Stretch*) Who's the employee with the most territories?
query('PRAGMA table_info (territory);')

employee_territory = """SELECT e.id, 
                        e.FirstName, e.LastName, 
                        COUNT(DISTINCT t.id)
                        FROM employee as e,
                        territory as t,
                        employeeterritory as et
                        WHERE e.id = et.employeeid AND 
                        et.TerritoryId = t.id
                        GROUP BY e.id 
                        ORDER BY 4 DESC
                        LIMIT 1;
"""

query(employee_territory)
