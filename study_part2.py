

import sqlite3
import os

FILEPATH = os.path.join(os.path.dirname(__file__),"Chinook_Sqlite.sqlite")

conn = sqlite3.connect(FILEPATH)

curs = conn.cursor()

# query1 = """
# SELECT * 
# FROM Album
# ;
# """

# result = conn.execute(query1).fetchall()

# print(result)

# ### Queries
# **Single Table Queries**
# 1. Find the average invoice total for each customer, return the details for the first 5 ID's
# 2. Return all columns in Customer for the first 5 customers residing in the United States
# 3. Which employee does not report to anyone?
# 4. Find the number of unique composers
# 5. How many rows are in the Track table?
# ​
# **Joins**
# ​
# 6. Get the name of all Black Sabbath tracks and the albums they came off of
# 7. What is the most popular genre by number of tracks?
# 8. Find all customers that have spent over $45
# 9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
# 10. Return the first and last name of each employee and who they report to