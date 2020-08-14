# Unit 3 Sprint 2 SQL and Databases Study Guide

This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. 
There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge 
as well as to be able to speak on these topics comfortably in interviews and on the job.

If you get stuck or are unsure of something remember the 20 minute rule. 
If that doesn't help, then research a solution with google and stackoverflow. Only once you have exausted these methods should you turn to your Team Lead - 
they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.
Have fun studying!
# SQL

## Questions of understanding
1. What is SQL?
    SQL is a programming language use to manage relational databases. 
    It's an industry standard that makes it easy to query information from tables. 
2. What is a RDBMS?
    Relational Database management systems store data ina  tabular format as opposed to a file format which enables there to be connection between peices of data. 
3. What is the ETL pipeline?
    A process by extracting data from one system, tranforming it, and loading into a place where it can be accessed like a data-warehouse or data-lake. 
4. What is a schema?
    Scheme refers to the relationship between objects in a database. Schema offers a means ot separate database objects from database users. 
5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
 - Atomicity: guarantee that transactions happen or they don't. 
 - Consistency: gurantees transactions are never half finished and that the constraints are never violated
 - Isolation: transactions cannot read data from other transactions that aren't yet completed. All transactions are executed sequentially rather than simultaneously. 
 - Durability: once a transaction has been completed it is gauranteed to be recorded. 
6. Explain each of the table relationships and give an example for each
 - One-to-One
    A relationship between two talbes where both tables are associated by one matching row. RPG characters are associated by character_id. 
 - One-to-Many
    A relationship between two tables where a row form one table can have multiple matching rows in a the other table. 
    In an rpg, the Item_id table would have multipel relationships to a character_inventory that has weapons, healing items, and misc items. 
 - Many-to-Many
    There exist many relationships between tables. Customers could purchase multiple products and products can be purcahsed by multiple customers. 

## Syntax
For the following section, give a brief explanation of each of the SQL commands.

1. **SELECT** - pick the columns from a table
2. **WHERE** - filter by integer, strings, or other conditions(x>30)
3. **LIMIT** - include only x number of rows
5. **JOIN** - Joins two tables together on a column or completely
6. **CREATE TABLE** - new table
7. **INSERT** - insert a row or new data into a table
8. **DISTINCT** - select only the 
9. **GROUP BY** - organize the selected data by a column(Date, money, customer)
10. **ORDER BY** - sort the data by a column(date, most recent customer)
11. **AVG** - return the avg of a selected column/data
12. **MAX** - return the max value
13. **AS** - relabled a column as something else. 

## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
2. Create a table with the following columns
```
 student - string
 studied - string
 grade - int
 age - int
 sex - string
 ```

3. Fill the table with the following data
```
 'Lion-O', 'True', 85, 24, 'Male'
 'Cheetara', 'True', 95, 22, 'Female'
 'Mumm-Ra', 'False', 65, 153, 'Male'
 'Snarf', 'False', 70, 15, 'Male'
 'Panthro', 'True', 80, 30, 'Male'
 ```
4. Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
5. Write the following queries to check your work. Querie outputs should be formatted for readability, don't simply print a number to the screen with no explanation, add context.
```
What is the average age? Expected Result - 48.8
What are the name of the female students? Expected Result - 'Cheetara'
How many students studied? Expected Results - 3
Return all students and all columns, sorted by student names in alphabetical order.
```

## Query All the Tables!

### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.

### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's
2. Return all columns in Customer for the first 5 customers residing in the United States
3. Which employee does not report to anyone?
4. Find the number of unique composers
5. How many rows are in the Track table?

**Joins**

6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. 
If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to

# NoSQL

## Questions of Understanding
1. What is a document store?
    A document oriented database is a program that stores and retreives information. 
    It is a subset of the key-value store which is a NoSQL concept. 
2. What is a key:value pair? What datatype in Python uses Key:Value pairs?
    A key:value pair is a method for storing data by which a key serves a unique identifier for a piece of data. 
    A dictionary is a common key-value pair used in python. 
3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database

4. What are some of the trade-offs between SQL and NoSQL?
One of the primary trade-offs between SQL and NoSQL is the scalability of these data structures. 
NoSQL scales vertically, meaning that if a network has a small number of nodes/endpoints then it may benefit from a NoSQL structure. This would be helpful for large entities that may only have to connect with a few networks. NoSQL also doesn't provide the ability to perform joins across tables, lacks standardized interfaces, and doesn't have the network effects that SQL like databases maintains. 

SQL databases scale horizontally where there are a large number of nodes. 
This is helpful for a network where many devices each act as their own node and need to be able to query data.  

5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
 - Basically: refers to data availability. If a node in the database fails then part of the data will be inaccessible, 
 however, the data layer/database will say operational. AKA the database works most of the time. 
 This is helpful if you have a system that is critical by nature, such as a government database. 
 - Available:
 - Soft state: Stores of data don't have to be mutually consistent at every point in time. The state of the database will change over time. 
 This means you could have data with multiple writes that do not match entirely. 
 - Eventual consistency: data should always be consistent with regards to how many changes are performed. However, this doesn't happen immediately. 

 Example. Social media doesn't immediately update the state of the social network (Twitter, Facebook, etc) because nobody is checking it. 
 It is more important to provide quick responses than to make sure everyone's state is updated.  