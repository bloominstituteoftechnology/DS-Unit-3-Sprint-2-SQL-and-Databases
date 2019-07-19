import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

def querydb(query):
    curs.execute(query)
    results = curs.fetchall()
    return results


# Questions

'''
What are the ten most expensive items (per unit price) in the database?
What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
(Stretch) How does the average age of employee at hire vary by city?

What are the ten most expensive items (per unit price) in the database and their suppliers?
What is the largest category (by number of unique products in it)?
(Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.

'''

if __name__ == '__main__':
    
    q1 = '''SELECT p.UnitPrice
            FROM Product as p
            ORDER BY UnitPrice DESC
            LIMIT 10'''
    
    print(f'The ten most expensive items per unit price are {querydb(q1)} \n')
  
    q2 = '''SELECT AVG(e.HireDate - e.BirthDate)
            FROM Employee as e'''
    
    print(f'The average age of each employee at the time of hire is {querydb(q2)[0][0]} \n')
   

    q3 = '''SELECT e.City, AVG(e.HireDate - e.BirthDate)
            FROM Employee as e
            GROUP BY e.City
            '''
    
    print(f'The average age per city is {querydb(q3)} \n')
  
    q4 = '''SELECT p.UnitPrice, s.CompanyName
                FROM Product as p
                JOIN Supplier as s
                ON p.SupplierId = s.id
                ORDER BY UnitPrice DESC
                LIMIT 10'''
    
    print(f'The ten most expensive items and their supplier are {querydb(q4)} \n')
 
    q5 = '''SELECT  c.CategoryName, COUNT(c.CategoryName) as cc
            FROM Category as c
            JOIN Product as p
            ON c.Id = p.CategoryId
            GROUP BY c.CategoryName
            ORDER BY cc DESC
            LIMIT 1'''
    
    print(f'The largest category is {querydb(q5)[0][0]} \n')
    
    q6 = '''SELECT e.id, COUNT(DISTINCT t.TerritoryId) as d
            FROM Employee as e
            JOIN EmployeeTerritory as t 
            ON e.id = t.EmployeeID
            GROUP BY e.id 
            ORDER BY d DESC
            LIMIT 1'''
    
    print(f'Employee {querydb(q6)[0][0]} has the most territories \n')
    