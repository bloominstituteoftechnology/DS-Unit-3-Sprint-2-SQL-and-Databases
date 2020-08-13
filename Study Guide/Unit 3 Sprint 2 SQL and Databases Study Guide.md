# Unit 3 Sprint 2 SQL and Databases Study Guide

This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. 
There are a mix of written questions and coding exercises, both are equally important to prepare you for the 
sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.

If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, 
then research a solution with [google](https://www.google.com) or [StackOverflow](https://www.stackoverflow.com). 
Only once you have exhausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. 
That being said, don't hesitate to ask for help if you truly are stuck.

Have fun studying!

## SQL

**Concepts:**

1. What is SQL?
- Selective Query Language: It is a simple way we can query databases in order to obtain the data we want from specific
tables or areas
2. What is a RDBMS?
- Relational Data Base Management System: These are systems that allow us to interact with a database: DB browser, Postgres
3. What is an ETL pipeline?
- Extract Transform Load: This is a way that DS takes data from one place and places it into another. 
-- Extract = Data out
-- Transform = Taking it from one form to another form
-- Load = taking it in that new form and inserting, or entering it into the new database or structure. 
4. What is a schema?
- Schema is a framework that ensures a structure for the database to accept certain formats of data - Deciding on 
datatypes, lengths of strings, and Primary keys when necessary

5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
	- **A**
	- **C**
	- **I**
	- **D**
6. Explain each of the table relationships and give an example for each
	- One-to-One: Country to Capital, for each instance there is one singular connection
	- One-to-Many: Book to Pages, for on instance there are many of the connection
	- Many-to-Many: Books to Authors, May Authors write many books and often interconnect on certain books. 

## Syntax
For the following section, give a brief explanation of each of the SQL commands.

1. **SELECT** - Specify the columns that are wanted FROM a certain table in the DB 
('SELECT character_id, name, level FROM charactercreator_character')
2. **WHERE** - A Joint logical condition. 
('WHERE character_id >10 AND LEVEL >10)
3. **LIMIT** - The amount of results you receive during the .fetachll() period
4. **ORDER** - Choosing a column in which the order is specified - can use number based columns and add DESC
5. **JOIN** - INNER, LEFT, RIGHT, MIDDLE also ON Allows for merging of table by different aspects. Inner is often preffered, 
because it allows for no missing values. Left can be useful for seeing the difference in certain tables. 
6. **CREATE TABLE** - When loading data there needs to be a table with a proper schema to load the data. 
7. **INSERT** -Using this allows to insert data into the table 
8. **DISTINCT** -Parameter used during SELECT that allows to only include values that are not repeats of another
9. **GROUP BY** -Using this will aid in an implicit join
10. **ORDER BY** -
11. **AVG** - 
12. **MAX** -
13. **AS** - Casting a specific section to a different ID in order to limit the amount of writing necessary for the query

## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`.
 Don't forget to be PEP8 compliant!
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

### Questions of Understanding

1. What is a document store?

2. What is a `key:value` pair? What data type in Python uses `key:value` pairs?

3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database

4. What are some of the trade-offs between SQL and NoSQL?

5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
    - B
    - A
    - S
    - E
