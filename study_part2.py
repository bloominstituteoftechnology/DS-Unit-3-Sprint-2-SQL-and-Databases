

import sqlite3
import os

FILEPATH = os.path.join(os.path.dirname(__file__),"Chinook_Sqlite.sqlite")

conn = sqlite3.connect(FILEPATH)

curs = conn.cursor()


# ### Queries
# **Single Table Queries**
# 1. Find the average invoice total for each customer, return the details for the first 5 ID's

query = """
SELECT
    CustomerId,
    CAST(ROUND(AVG(Total),2) AS DEC(10,2))
    avg_total
FROM
    Invoice
GROUP BY
    CustomerId
ORDER BY
    CustomerId
LIMIT 5;
"""
result = conn.execute(query).fetchall()

print ("---------------------------")
print("Customer 1 Avg Total: ", result[0][1])
print("Customer 2 Avg Total: ", result[1][1])
print("Customer 3 Avg Total: ", result[2][1])
print("Customer 4 Avg Total: ", result[3][1])
print("Customer 5 Avg Total: ", result[4][1])
print ("---------------------------")


# 2. Return all columns in Customer for the first 5 customers residing in the United States


query1 = """
SELECT *
FROM
    Customer
WHERE
    Country = "USA"
ORDER BY CustomerId ASC
LIMIT 5;
"""
result1 = conn.execute(query1).fetchall()

print("Customer 1 Columns: ", result1[0][0:13])
print ("------------------------------------------------------")
print("Customer 2 Columns: ", result1[1][0:13])
print ("------------------------------------------------------")
print("Customer 3 Columns: ", result1[2][0:13])
print ("------------------------------------------------------")
print("Customer 4 Columns: ", result1[3][0:13])
print ("------------------------------------------------------")
print("Customer 5 Columns: ", result1[4][0:13])
print ("------------------------------------------------------")


# 3. Which employee does not report to anyone?

query2 = """

SELECT EmployeeId,
    FirstName
    LastName
FROM Employee
WHERE ReportsTo IS NULL
"""

result2 = conn.execute(query2).fetchall()

print ("Employee who does not report: ", result2)

print ("----------------------------------------------")


# 4. Find the number of unique composers

query3 = """

SELECT DISTINCT COUNT(Composer)
FROM Track
"""

result3 = conn.execute(query3).fetchall()

print ("Number of unique composers: ", result3)

print ("----------------------------------------------")


# 5. How many rows are in the Track table?

query4 = """
SELECT COUNT(*)
FROM Track
"""

result4 = conn.execute(query4).fetchall()

print ("Number track rows: ", result4)

print ("------------------------------")


# **Joins**

# 6. Get the name of all Black Sabbath tracks and the albums they came off of

query4 = """
SELECT COUNT(*)
FROM Track
"""

result4 = conn.execute(query4).fetchall()

print ("Number track rows: ", result4)

print ("------------------------------")


# 7. What is the most popular genre by number of tracks?


# 8. Find all customers that have spent over $45
# 9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
# 10. Return the first and last name of each employee and who they report to