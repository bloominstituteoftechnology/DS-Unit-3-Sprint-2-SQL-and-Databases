
import sqlite3
import pandas as pd

db_name = 'northwind_small.sqlite3'
conn = sqlite3.connect(db_name)
curs = conn.cursor()

############################################################
print("""
  SELECT name FROM sqlite_master
   WEHRE type='table'
ORDER BY name; 
""")
print(curs.execute("SELECT name FROM sqlite_master \
WHERE type='table' \
ORDER BY name;").fetchall())

print("""
SELECT sql FROM sqlite_master
 WHERE name="Customer";
""")
print(curs.execute('SELECT sql FROM sqlite_master \
WHERE name="Customer";').fetchall()[0][0])
print()

############################################################
# start from here I am not going to capitalize the SQL 
# tokens cause it is really unnecessary for practice...
############################################################

############################################################
print("""
What are the ten most expensive items (per unit price) \
in the database?
""")
sql = """
  select ID, ProductName, UnitPrice
    from Product
order by UnitPrice desc limit 10
"""
with pd.option_context('display.max_rows', None, 
                       'display.max_columns', None):
    print(pd.read_sql(sql, conn))
print()

############################################################
print("""
What is the average age of an employee at the time of \
their hiring? (Hint: a lot of arithmetic works with \
dates.)
""")
sql = """
select ID, FirstName, LastName, 
       HireDate - BirthDate as HireAtAge
  from Employee
"""
with pd.option_context('display.max_rows', None, 
                       'display.max_columns', None):
    print(pd.read_sql(sql, conn))
print()

############################################################
print("""
(Stretch) How does the average age of employee \
at hire vary by city?
""")
sql = """
select avg(HireAtAge), City 
from (
    select HireDate - BirthDate as HireAtAge,
           City
      from Employee
)
group by City
"""
with pd.option_context('display.max_rows', None, 
                       'display.max_columns', None):
    print(pd.read_sql(sql, conn))
print()

############################################################
print("""
What are the ten most expensive items (per unit price) \
in the database and their suppliers?
""")
sql = """
   select p.ID, p.ProductName, p.UnitPrice,
          s.CompanyName as Supplier
     from Product as p
left join Supplier as s
       on p.SupplierID = s.ID
 order by p.UnitPrice desc limit 10
"""
with pd.option_context('display.max_rows', None, 
                       'display.max_columns', None):
    print(pd.read_sql(sql, conn))
print()

############################################################
print("""
What is the largest category \
(by number of unique products in it)?
Note: I could have used max(). But I think in real life \
people usually want to see a list (report).
""")
sql = """
   select Count(c.ID) as ProductTypes,
          c.ID,
          c.CategoryName
     from Category as c
left join Product as p
       on c.ID = p.CategoryID
 group by c.ID
 order by ProductTypes desc
    limit 1
"""
with pd.option_context('display.max_rows', None, 
                       'display.max_columns', None):
    print(pd.read_sql(sql, conn))
print()

############################################################
print("""
(Stretch) Who's the employee with the most territories? \
Use TerritoryId (not name, region, or other fields) \
as the unique identifier for territories.
""")
sql = """
  select t.EmployeeID,
         t.TerritoryCount,
         e.FirstName,
         e.LastName
    from (
            select EmployeeID,
                   count(TerritoryID) as TerritoryCount
              from EmployeeTerritory
          group by EmployeeID
          order by TerritoryCount desc
             limit 1
         ) as t
left join Employee as e
       on t.EmployeeID = e.ID
"""
with pd.option_context('display.max_rows', None, 
                       'display.max_columns', None):
    print(pd.read_sql(sql, conn))
print()