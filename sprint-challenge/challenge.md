# Data Science Unit 3 Sprint Challenge 2

## Databases and SQL

A SQL Query walks into a bar. In one corner of the bar are two tables. The Query
walks up to the tables and asks:

...

*"Mind if I join you?"*

---

In this sprint challenge you will write code and answer questions related to
databases, with a focus on SQL but an acknowledgment of the broader ecosystem.
You may use any tools and references you wish, but your final code should
reflect *your* work and be saved in `.py` files (*not* notebooks), and (along
with this file including your written answers) added to your
`DS-Unit-3-Sprint-2-SQL-and-Databases` repo.

For all your code, you may only import/use the following:
- other modules you write
- `sqlite3` (from the standard library)

As always, make sure to manage your time - get a section/question to "good
enough" and then move on to make sure you do everything. You can always revisit
and polish at the end if time allows.

This file is Markdown, so it may be helpful to add/commit/push it first so you
can view it all nice and rendered on GitHub.

Good luck!

### Part 1 - Making and populating a Database

Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 3!

      Number of rows: 3

- How many rows are there where both `x` and `y` are at least 5?

      Number of rows w/ x >= 5 and y >= 5:  2

- How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?

      Number of distinct y values:  2

Your code (to reproduce all above steps) should be saved in `demo_data.py` and
added to the repository along with the generated SQLite database.

### Part 2 - The Northwind Database

Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.

![Northwind Entity-Relationship Diagram](./northwind_erd.png)

Above is an entity-relationship diagram - a picture summarizing the schema and
relationships in the database. Note that it was generated using Microsoft
Access, and some of the specific table/field names are different in the provided
data. You can see all the tables available to SQLite as follows:

```python
>>> curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
```

Unlike the diagram, the tables in SQLite are singular and not plural (do not end
in `s`). And you can see the schema (`CREATE TABLE` statement) behind any given
table with:
```python
>>> curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
"CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
"ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
```

In particular note that the *primary* key is `Id`, and not `CustomerId`. On
other tables (where it is a *foreign* key) it will be `CustomerId`. Also note -
the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that
particular table, but it's a good lesson in the danger of keyword conflicts.

Answer the following questions (each is from a single table):

- What are the ten most expensive items (per unit price) in the database?

  Top 10 most expensive products:
  * Côte de Blaye: 263.5
  * Thüringer Rostbratwurst: 123.79
  * Mishi Kobe Niku: 97
  * Sir Rodney's Marmalade: 81
  * Carnarvon Tigers: 62.5
  * Raclette Courdavault: 55
  * Manjimup Dried Apples: 53
  * Tarte au sucre: 49.3
  * Ipoh Coffee: 46
  * Rössle Sauerkraut: 45.6

- What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)

  Average age at hiring date of employees:
    
      37.22222222222222

- (*Stretch*) How does the average age of employee at hire vary by city?

  Average age at hiring date of employees by city:
  * Kirkland: 29.0
  * London: 32.5
  * Redmond: 56.0
  * Seattle: 40.0
  * Tacoma: 40.0

Your code (to load and query the data) should be saved in `northwind.py`, and
added to the repository. Do your best to answer in purely SQL, but if necessary
use Python/other logic to help.

### Part 3 - Sailing the Northwind Seas

You've answered some basic questions from the Northwind database, looking at
individual tables - now it's time to put things together, and `JOIN`!

Using `sqlite3` in `northwind.py`, answer the following:

- What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?

  Top 10 most expensive products with company name:
  * Côte de Blaye [Aux joyeux ecclésiastiques]: 263.5
  * Thüringer Rostbratwurst [Plutzer Lebensmittelgroßmärkte AG]: 123.79
  * Mishi Kobe Niku [Tokyo Traders]: 97
  * Sir Rodney's Marmalade [Specialty Biscuits, Ltd.]: 81
  * Carnarvon Tigers [Pavlova, Ltd.]: 62.5
  * Raclette Courdavault [Gai pâturage]: 55
  * Manjimup Dried Apples [G'day, Mate]: 53
  * Tarte au sucre [Forêts d'érables]: 49.3
  * Ipoh Coffee [Leka Trading]: 46
  * Rössle Sauerkraut [Plutzer Lebensmittelgroßmärkte AG]: 45.6

- What is the largest category (by number of products in it)?

  Category w/ most products:
      
      Confections: 13

- (*Stretch*) What are the top five territories (by number of employees), and
  how many employees do they have?

  Top 5 employees with most territories:
  * Mr. Robert King: 10
  * Dr. Andrew Fuller: 7
  * Mr. Steven Buchanan: 7
  * Ms. Anne Dodsworth: 7
  * Mr. Michael Suyama: 5

### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

#### Part 4 Answers

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

  The type of relationship between the `Employee` and `Territory` tables is
  that of one-to-one, where each row in the `Employee` table correspond
  to one row in the `Territory` table and vice-versa.
  
  In this case, the intermediary table is `EmployeeTerritory`, and the
  relathionship between `Employee` and `EmployeeTerritory` is one-to-one
  through `Employee.Id` and `EmployeeTerritory.EmployeeID`, and
  `EmployeeTerritory` to `Territory` is one-to-one through
  `EmployeeTerritory.TerritoryID` and `Territory.Id`. Together, this makes the
  relationship one-to-one.

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?

  A document store is appropriate in use for mobile and social networking sites.
  This is because it is much faster than standard RDBMS systems when dealing
  with large amounts of data, especially when needing scalable performance,
  that need to be retrieved quickly and there is not a high need for each
  transaction to be done completely sequentially.

  A document store is not appropriate when there is a need for transactions to
  absolutely be done sequentially, especially in banking situations, where 2
  transactions occurring simultaneously can lead to incorrect balances or
  transactions beween accounts creating possible errors.

- (*Stretch*) What is "NewSQL", and what is it trying to achieve?

  NewSQL is basically a combination of old SQL reliability (ACID) and NoSQL
  scalable performance. It relies heavily on the relational data model of old
  SQL as well as having SQL as the query language. The most mature NewSQL
  system is probably VoltDB, but there are some disadvantages to this model as
  well. Firstly, it is not as general-purpose as SQL, where there needs to be
  serious planning in how the system is used. As well as this, if it is dealing
  with huge amounts of data, it is not as good as NoSQL, as it could require
  terabytes of memory (RAM) for storing certain volumes of data.

### Part 5 - Turn it in!
Add all the files you wrote (`buddymove_holidayiq.py`, `northwind.py`), as well
as this file with your answers to part 7, to your weekly repo
(`DS-Unit-3-Sprint-2-SQL-and-Databases`). Commit, push, and await feedback from
your PM. Thanks for your hard work!

If you got this far, check out the [larger Northwind
database](https://github.com/jpwhite3/northwind-SQLite3/blob/master/Northwind_large.sqlite.zip) -
your queries should run on it as well, with richer results.
