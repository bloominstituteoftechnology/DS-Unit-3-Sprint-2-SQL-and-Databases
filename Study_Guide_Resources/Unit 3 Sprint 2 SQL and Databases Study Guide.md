# Unit 3 Sprint 2 SQL and Databases Study Guide

This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.

If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with [google](https://www.google.com) or [StackOverflow](https://www.stackoverflow.com). Only once you have exhausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.

Have fun studying!

## SQL

**Concepts:**

1. What is SQL?
Structure Query Language
2. What is a RDBMS?
- Relational Data Base Management System
The data in RDBMS is stored in database objects called tables.
A table is a collection of related data entries and it consists of columns and rows.

3. What is an ETL pipeline?
- Means Extract Transform Load
- Extracting data from different sources, 

4. What is a schema?
- Finally the information which is now available in a consistent format gets loaded. From now one you can obtain any 
specific piece of data and compare it in relation to any other pieces of data. 

5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
In the context of transaction processing, the acronym ACID refers to the four key properties of a transaction: atomicity, consistency, isolation, and durability.

- Atomicity
All changes to data are performed as if they are a single operation. That is, all the changes are performed, or none of them are.
For example, in an application that transfers funds from one account to another, the atomicity property ensures that, if a debit is made successfully from one account, the corresponding credit is made to the other account.
- Consistency
Data is in a consistent state when a transaction starts and when it ends.
For example, in an application that transfers funds from one account to another, the consistency property ensures that the total value of funds in both the accounts is the same at the start and end of each transaction.
- Isolation
The intermediate state of a transaction is invisible to other transactions. As a result, transactions that run concurrently appear to be serialized.
For example, in an application that transfers funds from one account to another, the isolation property ensures that another transaction sees the transferred funds in one account or the other, but not in both, nor in neither.
- Durability 
After a transaction successfully completes, changes to data persist and are not undone, even in the event of a system failure.
For example, in an application that transfers funds from one account to another, the durability property ensures that the changes made to each account will not be reversed.

6. Explain each of the table relationships and give an example for each
'https://medium.com/@emekadc/how-to-implement-one-to-one-one-to-many-
and-many-to-many-relationships-when-designing-a-database-9da2de684710'
	- One-to-One
When a row in a table is related to only one role in another table and vice versa,we say
 that is a one to one relationship. This relationship can be created using Primary key-Unique foreign key constraints.
For instance a Country can only have one UN Representative, and also a UN Representative
can only represent one Country.
	- One-to-Many
One to Many Relationship (1:M)
This is where a row from one table can have multiple matching rows in another table this relationship is defined as a one to many relationship. This type of relationship can be created using Primary key-Foreign key relationship.
This kind of Relationship, allows a Car to have multiple Engineers.
	- Many-to-Many
A row from one table can have multiple matching rows in another table, and a row in the other table can also have multiple matching rows in the first table this relationship is defined as a many to many relationship. This type of relationship can be created using a third table called “Junction table” or “Bridging table”. This Junction or Bridging table can be assumed as a place where attributes of the relationships between two lists of entities are stored.
This kind of Relationship, allows a junction or bridging table as a connection for the two tables.

## Syntax
For the following section, give a brief explanation of each of the SQL commands.

1. **SELECT** - 
2. **WHERE** - 
3. **LIMIT** - 
4. **ORDER** -
5. **JOIN** -
6. **CREATE TABLE** - 
7. **INSERT** -
8. **DISTINCT** -
9. **GROUP BY** -
10. **ORDER BY** -
11. **AVG** - 
12. **MAX** -
13. **AS** -

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
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to

## NoSQL
https://www.unitedglobalgrp.com/uncategorized/to-sql-or-to-nosql/#:~:text=The%20most%20significant%20trade%2Doff,systems%20%E2%80%93%20i.e.%20relational%20databases%20vs.&text=NoSQL%20databases%20do%20not%20require,spent%20preparing%20data%20%5B7%5D.
Unless u have a reason to scale -- go with traditional sql
If u have relational data go with postgress


### Questions of Understanding

1. What is a document store?
https://www.mongodb.com/document-databases

What is a Document Database?
Built around JSON-like documents, document databases are both natural and flexible for developers to work with. They promise higher developer productivity,
 and faster evolution with application needs. As a class of non-relational, sometimes called NoSQL database, 
the document data model has become the most popular alternative to tabular, relational databases.

1. Intuitive Data Model: Faster and Easier for Developers
Documents map to the objects in your code, so they are much more natural to work with. There is no need to decompose 
data across tables, run expensive JOINs, or integrate a separate ORM layer.
 Data that is accessed together is stored together, 
so you have less code to write and your users get higher performance.

2. What is a `key:value` pair? What data type in Python uses `key:value` pairs?

3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database

4. What are some of the trade-offs between SQL and NoSQL?
The most significant trade-off between SQL and NoSQL systems – i.e. relational databases vs. "everything else" – is the security and trustworthiness of vital, operational data for the agility, scalability and flexibility of big data.  Relational databases are specialized to structure data in a specific, well-defined, well-organized model [9].  Because they fully support ACID principles, transactions are not only highly reliable, the database also guarantees crash recovery.  The security risks that do exist are defined, and new research and product iterations continually improve against these gaps [9].  However, the same fail-saves that guarantee data also restrain performance [6].  The relational database stores multiple copies of data, which is centralized and unencrypted; in this way, the RDBMS is both inefficient and vulnerable to fraud, error and security attacks [3].

NoSQL databases do not require pre-defined schema, relationships or keys; less complex models translate to less time spent preparing data [7]. 
 Additionally, that NoSQL systems don’t fully support ACID principles also translates into faster performance
 of storing and retrieving data [7].  Theses performance-focused design features lend themselves particularly to the manipulation of Big Data.  
 At the same time, however, their design leaves security as an afterthought [9]. 
  Because NoSQL systems cannot be evaluated using ACID, transaction reliability is not natively assured [5, 6, 9]. 
   Where ACID principles are programmed into NoSQL systems, designers face a performance vs. consistency 
  trade-off – i.e. performance is negatively affected [6].  Further, there is some research that indicates a wide variation
   in the distribution of NoSQL database performance measures based on the type of operation
   performed, as well as the number of
   synchronous users [8].  Without ACID support, changes made in close proximity
 can overwrite other changes made within the database, especially if they occur close in time.

5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
    - B
    - A
    - S
    - E
