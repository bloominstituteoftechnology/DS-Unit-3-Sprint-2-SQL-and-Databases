"""
Part Four: Sql and Databases Sprint Challenge
Jason Meil DS3 Sprint 3 Unit 2 - 06.07.2019
"""
Questions (and your Answers)
Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

In the Northwind database, what is the type of relationship between the Employee and Territory tables?

In the Northwind Database the type of relationship between the above two tables is considered many to many.  According to Techopedia , a many-to-many relationship refers to a relationship between tables in a database when a parent row in one table contains several child rows in the second table, and vice versa. So as an example in this case; an employee can have more than one territory, and a territory can have more than one employee. Combining this relationship in the EmployeeTerritories table is utilized to provide lots of unique, interpretable values. And this makes it easier to interpret.

What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

So MongoDB like other document stores is a Obj Orient Database - NoSQL.  These types of databases are appropriate when there is a very quick turn over or change in data quickly or if data is continuously being streamed and dumped or collected but the order of the data is not clear (e.g. a data lake)  NoSQL provides a flexibility in data collection but it gives on order and readability.  Contrarily, NoSQL dbs are generally inappropriate when the data collection can or needs to be ordered and rigid. This is where you would need a Relational dbs (SQL) provide structure and predictability (e.g. a credit card provider collecting customer information).
