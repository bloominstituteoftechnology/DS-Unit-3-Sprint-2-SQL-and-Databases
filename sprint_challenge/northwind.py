
import sqlite3
import pandas as pd

database = "northwind_small.sqlite3"

# This is my query runner. It connects to the database, runs the query, 
# and formats the output as a table. 
def query_w_named_columns(query, db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    print("Query Result:\n", 
          pd.DataFrame(data, 
          columns=data[0].keys()).to_string(index=False))
    print("\n")
    cur.close 
    conn.close

# Here I write my queries
ten_most_expensive= """
SELECT ProductName AS Top_10_Products, 
       UnitPrice AS Product_Price
  FROM Product
 ORDER BY UnitPrice DESC
 LIMIT 10
"""

average_age_at_hiring="""
SELECT AVG (HireDate - BirthDate) AS Employee_Average_Age_When_Hired
  FROM Employee
"""

average_age_at_hiring_by_City="""
SELECT City, AVG (HireDate - BirthDate) AS Employee_Average_Age_When_Hired
  FROM Employee
 GROUP BY City
"""

ten_most_expensive_w_Supplier= """
SELECT ProductName AS Top_10_Products, 
       UnitPrice AS Product_Price,
       CompanyName as Supplier
  FROM Product
 INNER JOIN Supplier ON Product.SupplierID = Supplier.Id
 ORDER BY UnitPrice DESC
 LIMIT 10
"""

top_category = """
SELECT CategoryName AS Largest_Category
  FROM (SELECT CategoryName, 
               COUNT (ProductName) AS Number_of_Products
        FROM Product
        INNER JOIN Category ON Product.CategoryID = Category.Id
        GROUP BY CategoryName)
 ORDER BY Number_of_Products DESC
 LIMIT 1
"""

top_territory="""
SELECT TopTerritory AS The_Top_Territory_Is,
       Number_of_Employees AS It_has_this_many_employees
  FROM (SELECT TerritoryDescription AS TopTerritory,
               COUNT(EmployeeID) AS Number_of_Employees
          FROM EmployeeTerritory
         INNER JOIN Territory ON EmployeeTerritory.TerritoryId = Territory.Id
         GROUP BY TerritoryDescription)
 ORDER BY Number_of_Employees DESC
 LIMIT 1
"""


# Here I run my queries:
print("\nNorthwind Database Query Runner\n *****NOW RUNNING QUERIES*****\n")

queries = [ten_most_expensive, average_age_at_hiring, average_age_at_hiring_by_City,ten_most_expensive_w_Supplier,top_category,top_territory]

questions = [
"What are the ten most expensive items (per unit price) in the database?",
"What is the average age of an employee at the time of their hiring?", 
"(Stretch) How does the average age of employee at hire vary by city?",
"What are the ten most expensive items (per unit price) in the database *and* their suppliers?",
"What is the largest category (by number of products in it)?",
"(Stretch) What is the top territory (by number of employees), and how many employees does it have?"]

def query_questions(queries_, questions_, database_):
    question_count = 0
    for query in queries_:
        print(questions_[question_count])
        question_count += 1
        query_w_named_columns(query, database_)

if __name__ == '__main__':
    query_questions(queries,questions,database)
