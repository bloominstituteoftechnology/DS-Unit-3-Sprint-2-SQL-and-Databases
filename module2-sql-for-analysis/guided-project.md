# Guided Project Walkthrough

**IMPORTANT NOTE**

The following Guided Project demonstrates using a cloud PostgreSQL service called ElephantDB, which has since stopped taking new sign ups, to accomplish the project's objectives.

In order to follow along, some adjustments must be made:

1. Use [Aiven.io](https://aiven.io/) instead of ElephantDB as demonstrated in Learning Objective 1 in this module.
2. Connect to and interact with your database from your Python code as demonstrated in Learning Objective 2.

Yesterday we used a simple local workflow with SQLite - today, we'll work on inserting the same RPG data into a more production-style PostgreSQL database running on a server. We will use [psycopg](http://initd.org/psycopg/), a Python library for connecting to PostgreSQL, and specifically we will install [psycopg2-binary](https://pypi.org/project/psycopg2-binary/).

Once we get the data inserted, we will continue exploring and querying like we did yesterday, first answering the same questions and then going deeper. We'll also explore some of the specific functions that are different in PostgreSQL than SQLite.

## What is ElephantSQL?

ElephantSQL is a browser-based tool for setting up a "managed" PostgreSQL database in an actual web server somewhere in the world without us having to go directly to AWS and set everything up (which can be complicated and a big hassle). It also provides us an interface to write queries against our Postgres database just like DB Browser did yesterday.

## Why are we using PostgreSQL

* Helps us experience what it's like to use another SQL dialect.
* Postgres is a lot more scalable than SQLite, it's made to work better with large amounts of data.
* It allows us to get the database off of our computer and get it running on a cloud server which is more authentic to how we'll interact with databases in the real world.
* We can practice moving our data from the sqlite DB to Postgres which is a type of data pipeline.

## Create an instance on ElephantSQL

Make a "Tiny Turtle" free plan. This will give us 20MB of database space to play around with. 20MB isn't a ton, but it's not a little either, we can store a fair amount of tables and records with 20MB.

## Make a folder and file to hold our data pipeline

Inside of the `DS##_databases` folder that we worked in yesterday, make a new sub-folder and call it `postgresql_example`. I'll be creating mine within a GitHub repository so that I can push my code and easily share it with you when we're done.

Make a new file inside of this folder called `pipeline.py`.

Download a [fresh copy](https://github.com/BloomInstituteOfTechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3) of the `rpg_db.sqlite3` database that we were working with yesterday and move it into your `postgresql_example` folder alongside your `pipeline.py`.

## Create a Virtual Environment for this project

Start up a virtual environment in the root `DS##_databases` folder and install a few packages.

`pipenv install pandas numpy psycopg2-binary`

`psycopg2` is a library that will help us connect to and interact with a hosted PostgreSQL database with Python. By using the binary file we are installing the package directly to our hardware. I've found that we get less dependency issues when we use the binary file, but besides that you can think of it like any other package that we would import. In fact, we won't specify the binary file when we import the package.

## Use `psycopg2` in a REPL

Import the package

`>>> import psycopg2`

Look at the module object for kicks.

`>>> psycopg2`

This will show us all of the items that live in the package scope including python internals, package inernals, modules, constants, classes, functions and variables.

`>>> dir(psycopg2)`

The help command will show us documentation related to items that live within the package. If we pass in any functions to the help function their docstring will be displayed.

`>>> help(psycopg2.connect)`

Now let's create variables for all of the different pieces of information that psycopg2 needs in order to connect to our remote database.

Replace anything in the `<>` with information from the "details" section of your ElephantSQL instance.

`>>> dbname = "<User & Default database>"`

`>>> user = "<User & Default database>"`

`>>> password = "<password>"`

`>>> host = "<Server>"`

Make the connection to the server. If you get any errors double check the values that you have saved to your variables

`>>> conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)`

Look at any items that live on the connection object's scope. You should se a `.cursor()` `method in the long list of stuff.

`>>> dir(conn)`

Make a cursor object

`>>> curs = pg_conn.cursor()`

Look at any items that live on the connection object's scope. You should se an `.execute()` function listed in the long list of stuff.

`>>> dir(curs)`

So you see that this process is very similar to what we did yesterday, the biggest difference being that our server lives in a remote database so we have to provide more than just the database name to connect with it, and there are some specific psycopg2 functions that we have to use to generate the connection and cursor, but that we're doing pretty much the same steps that we did yesterday in our Python file. In fact, lets move our work into a more permanent .py file now.

```python
import psycopg2

dbname = "<User & Default database>"
user = "<User & Default database>"
password = "<password>"
host = "<Server>"

conn = psycopg2.connect(name=name, user=user, password=password, host=host)

curs = conn.cursor()

def execute_query(curs, query):
    result = curs.execute(query)
    return result
```

## Make a file to hold your queries

Make a file called `queries.py` that we can import into `postgresql_example` to get access to our queries.

Today we're not just going to write queries to retrieve data from the database, we're also going to write queries to create new tables, schemas, and to insert data into the database.

```python
'''Queries for sqlite to Postgres pipeline'''

create_table = '''
    CREATE TABLE test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        number INT
    );
'''

insert_data = """
INSERT INTO test_table (name, number)
VALUES ('A row name', 6), ('Another row', 72);
"""

select_all = '''SELECT * FROM test_table;'''
```

## Try out our new queries in a REPL

`>>> from queries import create_table, insert_data, select_all`

`>>> from pipeline import curs, execute_query`

`>>> execute_query(curs, create_table)`

Verify that the table creation worked by going to ElephantSQL, visiting the "BROWSER" tab and running the query `SELECT * FROM test_table;`

`>>> execute_query(curs, insert_data)`

`>>> execute_query(curs, select_all)`

## Create a pipeline for our RPG data

Now that we want to create a pipeline to take our RPG data and put it into a postgres database we're going to need to connect to both our SQLite DB and our Postgres DB at the same time and then use queries to more the information between the two.

```python
import psycopg2
import sqlite3
from queries import *

# Connecting to PostgreSQL DB

dbname = "<User & Default database>"
user = "<User & Default database>"
password = "<password>"
host = "<Server>"

pg_conn = psycopg2.connect(name=name, user=user, password=password, host=host)

pg_curs = conn.cursor()

# Connecting to SQLite DB

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Generic execute_query function that can work with either cursor object

def execute_query(curs, query=select_all):
    result = curs.execute(query)
    return result.fetchall()

```

Now in our `queries.py` file we can create SQLite queries to pull data out of `rpg_db.sqlite3` and insert that data into the Postgres DB.

```python
# sqlite queries
row_count = '''
SELECT COUNT(*)b
FROM charactercreator_character;
'''
```

## Test out the new query in the REPL

`>>> from queries import row_count`

`>>> from pipeline import sl_curs, execute_query`

`>>> execute_query(sl_curs, row_count)`

## Write a query to transfer `charactercreator_character` from sqlite to postgres

Add the following queries to `queries.py`

```python
get_characters = '''
SELECT * from charactercreator_character;
'''

get_character_table_info = '''
PRAGMA table.info(charactercreator_character);
'''

create_character_table = '''
CREATE TABLE IF NOT EXISTS charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);'''
```

Back in our `pipeline.py`

```python
'''Data Pipeline for moving sqlite db to postgres hosted db'''

import psycopg2
import sqlite3
from queries import *

# Connecting to PostgreSQL DB

dbname = "qbdybhyz"
user = "qbdybhyz"
password = "1cfJTjNLXvazVHYp_RhAyts0QtW_hnlo"
host = "fanny.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

# Connecting to SQLite DB

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Generic execute_query function that can work with either cursor object

def execute_query(curs, query=select_all):
    result = curs.execute(query)
    return result

def populate_pg_character_table(curs, conn, characters_list):
    for character in characters_list:
        insert_statement = '''
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {};
        '''.format(character[1:])
        curs.execute(insert_statement)
        conn.commit()


if __name__ == '__main__':    
    SL_CHARACTERS = execute_query(sl_curs, get_characters).fetchall()
    print(SL_CHARACTERS[:5])

    execute_query(pg_curs, create_character_table)

    populate_pg_character_table(pg_curs, pg_conn, SL_CHARACTERS)
```
