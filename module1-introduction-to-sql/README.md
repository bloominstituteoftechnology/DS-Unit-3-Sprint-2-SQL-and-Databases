# Sprint 2 Module 1 - Introduction to SQL

We will be introduced to the basics of Structured Query Language (SQL) - SQL is the primary tool used to connect to a relational database.

## Learning Objectives

- Write basic SQL queries to get specific subsets of data from a database and
  answer basic "business questions"
- Understand the purpose of SQL join, and perform joins to access data from
  multiple tables

## Before Lecture

The Python Standard Library includes a module
[sqlite3](https://docs.python.org/3/library/sqlite3.html), an API for data
persistence via the SQLite - a simple disk-based database that doesn't require a
separate server process. Read the tutorial, and try the given examples. See if
you can modify them in simple ways, and come with questions!

Also, check out the [DB Browser for SQLite](https://sqlitebrowser.org) - we'll
emphasize using `sqlite3` from Python so we can do things programmatically, but
it is encouraged to install the DB Browser as a helpful utility for ad hoc
inspection and querying.

## Live Lecture Task

[See guided-project.md](https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/guided-project.md)

## Assignment

[See assignment.md](https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/assignment.md)

## Stretch Goals

## Resources

For a more complicated example SQLite database with a number of tables to play
with, check out this [SQLite Sample
Database](https://www.sqlitetutorial.net/sqlite-sample-database/).

The RPG data also exists in a [JSON
file](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json) -
try loading it with the standard [json
module](https://docs.python.org/3.5/library/json.html), and reproducing the
above queries with direct manipulation of the Python dictionaries. Also, try to
load it into a `pandas` dataframe and reproduce the above queries with
appropriate dataframe function calls.
