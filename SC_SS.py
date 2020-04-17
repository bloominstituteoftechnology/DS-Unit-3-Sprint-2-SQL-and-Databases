This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.
​
If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with google and stackoverflow. Only once you have exausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.
​
Have fun studying!
​
​
# SQL
​
## Questions of understanding
1. What is SQL?

        # Structured Query Language - a language for interacting with data bases.
2. What is a RDBMS?

        # Relation Database Mgmt System - A database mgmt system designed for relational databases - data that is stored in
        # a structured format using rows and columns with data that is "related".
3. What is the ETL pipeline?
        # Set of processing elements that moves data from one system to another.

4. What is a schema?
        # The organization of the data in a database.

5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
 - Atomicity -  if any of the statements constituting a transaction fails to complete, the entire transaction fails and the database is left unchanged.
 - Consistency - Consistent (the change can only happen if the new state of the system will be valid; 
                any attempt to commit an invalid change will fail, leaving the system in its previous valid state
 - Isolation - ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially
 - Durability - guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure (e.g., power outage or crash).

6. Explain each of the table relationships and give an example for each
 - One-to-One: One item in a table is equally represented by one item in another table... character_id to character_id
 - One-to-Many: One item in a table is represented by multiple items in a another table... birthday to many people having that birthday. A customers purchases.
 - Many-to-Many: customers can purchase various products, and products can be purchased by many customers.
​
## Syntax
For the following section, give a brief explanation of each of the SQL commands.
​
1. **SELECT** -  SELECT statements are used to fetch data from a database. Every query will begin with SELECT.
2. **WHERE** -  WHERE is a clause that indicates you want to filter the result set to include only rows where the following condition is true.
3. **LIMIT** - LIMIT is a clause that lets you specify the maximum number of rows the result set will have.
4. **ORDER** - ORDER BY is a clause that indicates you want to sort the result set by a particular column either alphabetically or numerically.
5. **JOIN** - An inner join will combine rows from different tables if the join condition is true. 
            An outer join will combine rows from different tables even if the join condition is not met. Every row in the left table is returned in the result set, 
            and if the join condition is not met, then NULL values are used to fill in the columns from the right table.
            The SQL LEFT JOIN returns all rows from the left table, even if there are no matches in the right table. This means that if the ON 
            clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table.
            The SQL RIGHT JOIN returns all rows from the right table, even if there are no matches in the left table. This means that if the ON 
            clause matches 0 (zero) records in the left table; the join will still return a row in the result, but with NULL in each column from the left table.
6. **CREATE TABLE** - CREATE TABLE creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.
7. **INSERT** - INSERT statements are used to add a new row to a table.
8. **DISTINCT** - Unique values of a column can be selected using a DISTINCT query.
9. **GROUP BY** - The GROUP BY clause is an optional clause of the SELECT statement that combines rows into groups based on 
            matching values in specified columns. One row is returned for each group.
10. **ORDER BY** - you specify the column in which you want to sort and the kind of the sort order - ASC and DESC
11. **AVG** - The SQL AVG function is an aggregate function that calculates the average value of a set. 
12. **MAX** - SQL provides the MAX function that allows you to find the maximum value in a set of values.
13. **AS** - The AS command is used to rename a column or table with an alias.
​
## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. 
The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
2. Create a table with the following columns
```
 student - string
 studied - string
 grade - int
 age - int
 sex - string
 ```
​
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
​
## Query All the Tables!
​
### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.
​
### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's
2. Return all columns in Customer for the first 5 customers residing in the United States
3. Which employee does not report to anyone?
4. Find the number of unique composers
5. How many rows are in the Track table?
​
**Joins**
​
6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to
​
# NoSQL
​
## Questions of Understanding
1. What is a document store?
Document stores, also called document-oriented database systems, are characterized by their schema-free organization of data.

That means:

Records do not need to have a uniform structure, i.e. different records may have different columns.
The types of the values â€‹â€‹of individual columns can be different for each record.
Columns can have more than one value (arrays).
Records can have a nested structure.


2. What is a key:value pair? What datatype in Python uses Key:Value pairs?

At the simplest level, a key-value pair is just two values, one of which you have 
designated to be a "key" and the other you have designated to be the "value".

Python uses dictionaries.

3. Give an example of when it would be best to use a SQL Database and 
when it would be best to use a NoSQL Database


Here’s the key difference when comparing SQL vs. NoSQL scalability: 
NoSQL engines are designed to scale out and leverage cloud computing. 
When scaling out or horizontally we are adding resources to a single node 
(a computer or server). We can have one database working on multiple nodes. 
Scaling out (or back in) means we can easily add and remove nodes. 
This makes NoSQL a perfect match for the cloud. Because it can scale out, 
you will be maximizing the scalability benefits of the cloud. 
You can run SQL on Azure, for example, but you will be limited in your ability to scale.

NoSQL pairs well with fast paced, agile development teams. It allows for 
rapid changes to the database schema as the scope evolves and requirements change.

Again, this doesn’t mean SQL is slow. If your data is highly structured and 
you anticipate minimal change then there’s probably no reason to use NoSQL. 


4. What are some of the trade-offs between SQL and NoSQL?

https://www.integrant.com/when-to-use-sql-vs-nosql/

5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
 - B
 - A
 - S
 - E

 Basically Available, Soft state, Eventual consistency

A BASE system gives up on consistency.

Basically available indicates that the system does guarantee availability, 
in terms of the CAP theorem.
Soft state indicates that the state of the system may change over time, even without input. 
This is because of the eventual consistency model.
Eventual consistency indicates that the system will become consistent over time, given 
that the system doesn't receive input during that time.