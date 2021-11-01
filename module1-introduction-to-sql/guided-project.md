# Sprint 2 Module 1 - Guided Project

We'll work together with SQLite in Python, making and exploring a simple
database and trying a range of basic queries. Focus will be on the following SQL
keywords:

- `SELECT` - how we choose which columns to get
- `WHERE` - how we set conditions on the rows to be returned
- `LIMIT` - when we only want a certain number of rows
- `ORDER` - when we want to sort the output
- `JOIN` - when we need data from multiple tables combined

We'll also learn about how to use `CREATE TABLE` to specify a schema for our
data, and `INSERT` statements to put data into a table. And lastly, we'll learn
how to calculate some basic statistics with `COUNT()`, `AVG()`, and `SUM()`,
organized using the keyword `GROUP`.

---

## Before the Guided Project

Make sure you have download [DB Browser for SQLite](v)

## Guided Project Walkthrough

### Make a new folder for this project

If you have installed Git and set up an SSH key, please create a new repository for today's Guided Project and clone it to your machine.

If you don't have Git and SSH keys installed yet, just create a new folder on your desktop using the `mkdir` command.

### Download the database for local use

[Download the `rgb_db.sqlite3` file](https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3) from this week's repository.

Within DB Browser, select the `Open Database` button and use the file browser to open the `rgb_db.sqlite3` file. Once you have it open, feel free to click through some of the table "Schemas" on the left-hand side. The table attributes with little gold key icons next to them are called "primary keys" and the ones with silver keys next to them are called "secondary keys." They are the most important fields in the database table.

You can refer to [this image](https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/schema.png) to see an overview of the structure of the rgb database.

The database keys are what controls the "relations" in this relational database. When any record is created in a database it has to have all of the elements required by the schema in that table. Note all of the "NOT NULL" indicators in the `schema.png` file. Each record within a table is assigned a primary ID at the moment that it is created. In the database's eyes this ID is how that record will be identified. The database is very fast at querying records by ID. Primary keys are assigned when we add a record to a table, secondary keys point to a record in a different table to relate those two items to each other.

From the command line navigate to your project repository and create a virtual environment by running `pipenv install`. If you don't indicate any libraries to be installed a pipfile will be created, it just won't have any dependencies listed.

Run `pipenv shell` to activate your virtual environment.

Make a new sub folder within the project folder called `module1-examples`.

Go ahead and open the root project folder in VS Code. You'll know that you've opened the right one if you can see your pipfile in the file browser within VS Code, if you just see your `module1-examples` folder then you've opened the wrong folder.

Make a new file within the `module1-examples` folder called `sqlite_example.py`.

Before we can get started with our queries we'll need to move `rgb_db.sqlite3` into the `module1-examples` folder (same level as your `sqlite_example.py` file.).

You can either do this manually, or you can use the "move" `mv` command from the command line. Navigate to your downloads or whever you have the file and then run:

`mv <file_to_move> <destination_folder_path>`

### Connect to the DB and execute a query

We can now get started writing some queries. We don't need to install any packages because SQLite3 comes bundled with our python install. Let's open a REPL and make our first database connection, curor, query, and pull our query results.

Start off by importing sqlite3 at the top of your file

```python
# Step 0 - import sqlite3
import sqlite3
```

```python
# Step 1 - Connect to the Database
# please triple check that your DB name is correct.
connection = sqlite3.connect("rpg_db.sqlite3")
```

If you try and connect to a database that doesn't exist (because you have a typo in the name or something). SQLite will simply create an empty database named what you have tried to connect to and will connect to it for you. So you won't get any error messages and you'll be very confused when you can't query from the database because it doesn't have any tables.

```python
# Step 2 - Make the "cursor"
cursor = connection.cursor()
```

The cursor is like our personal SQL query butler that does whatever we ask it to. Whenever we make a query the cursor will go into the database, execute the query, and return to us any information from the query.

```python
# Step 3 - Write your query
query = 'SELECT * FROM charactercreator_character;'
```

The `SELECT *` query will get us all of the tables and rows from an indicated table. Please note the semicolon at the end of our query. This tells SQL that our query has ended and is a critical piece of syntax to include in all queries. Please also note that SQL keywords like SELECT and FROM are in all-caps. This a strong convention when writing SQL queries, but is not required but strongly encouraged.

```python
# Step 4 - Execute your query on the cursor
cursor.execute(query)
```

The cursor runs off and executes our query by grabbing the information out of the database. We now need to get that information out of the cursor by "pulling the results."

```python
# Step 5 - Pull the results from the cursor
results = cursor.fetchall()
```

The results of the table will be a list of tuples where each row or "record" in the database table gets its own tuple of values.

```python
# take a look at the first 5 items in the results list
results[:5]
```

### Move our query into a .py file

After trying the above commands out in a REPL, move them into your `sqlite_example.py` file. However, because we may end up with multiple queries, we're going to make a small change in renaming our query variable `select_all`.

```python
# Step 0 - import sqlite3
import sqlite3

# Step 1 - Connect to the Database
# please triple check that your DB name is correct.
connection = sqlite3.connect("rpg_db.sqlite3")

# Step 2 - Make the "cursor"
cursor = connection.cursor()

# Step 3 - Write your query
select_all = 'SELECT * FROM charactercreator_character;'

# Step 4 - Execute your query on the cursor
cursor.execute(select_all)

# Step 5 - Pull the results from the cursor
results = cursor.fetchall()
```

Make a new file called `queries.py` in your `module1-examples` folder. We'll use this file to hold many different queries as we practice running them. Move your select_all query into this file.

```python
select_all = '''
SELECT * 
FROM charactercreator_character;
'''
```

We can now import this `queries.py`  into `sqlite_example.py` and the select_all query will be available through whatever we name the query object.

`import queries as q`

Rewrite your step 4 to use the imported query module

`cursor.execute(q.select_all)`

Now we can write even more queries in the `queries.py` file and then execute them in the `sqlite_example.py` file.

### Create a db, table and insert records

```python
import sqlite3

# make a cursor and a connection to a new database.
conn = sqlite3.connect('mock_db.squlite3')
curs = conn.cursor()

# CREATE
create_statement = 'CREATE TABLE test_table (name char(20), age int);'

curs.execute(create_statement)

# READ - (SELECT)
select_all = 'SELECT * FROM test_table;'
curs.execute(select_all)
curs.fetchall()

# UPDATE - (INSERT INTO)
insert_statement = 'INSERT INTO test_table (name, age) VALUES ("Jimmy", 12);'
curs.execute(insert_statement)

# READ - (SELECT)
curs.execute(select_all)
curs.fetchall()

# DELETE

# saves all the changes made by a cursor on this connection channel Permanently alters the database's sqlite3 file. 
conn.commit()
# close your cursor when you're done
curs.close()
```

## Upgrade our approach with python functions

Now that we've experienced some of the commands needed for basic CRUD operations, lets go back to our `sqlite_example.py` file and use some python functions to make our approach a little bit more sophisticated.

```python
import sqlite3
import queries as q

# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# Make cursor and execute query function
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results

if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5])
```

You now have some slick files set up. One file for writing your queries in, and the other file for executing those queries and printing the results. Our functions have allowed us to boil down the somewhat repetitive original 5 steps of connecting to a database to just two function calls.

### Practice a bunch more queries in DB Browser

When we write the queries directly in DB Browser we don't have to wrap the in quotation marks, however we *will* need to write them as strings if we're creating the queries in a .py file.

### Get all records

`SELECT * FROM charactercreator_character;`

### Get the number of records in the table

`SELECT COUNT(*) FROM charactercreator_character;`

### get all unique names

`SELECT DISTINCT(name) FROM charactercreator_character;`

### count the number of unique names

`SELECT COUNT(DISTINCT(name)) FROM charactercreator_character;`)

### get specific columns

`SELECT name,hp FROM charactercreator_character;`

### Get a certain number of records using "LIMIT"

Now that our queries are getting longer we'll start making the multi-line for increased readability.

```SQL
SELECT name,hp 
FROM charactercreator_character 
LIMIT 10;
```

### Select specific rows using "WHERE"

```SQL
SELECT *
FROM charactercreator_character 
WHERE character_id > 80;
```

### Get a specific record

```SQL
SELECT character_id,name
FROM charactercreator_character 
WHERE character_id = 80;
```

### Get just character_id and name

```SQL
SELECT character_id,name
FROM charactercreator_character 
WHERE character_id > 80;
```

DB Browser might not like spaces between the values of your condition, you may need to write it as `character_id>80`.

### more complex conditions using "AND" or "OR"

```SQL
SELECT character_id,name
FROM charactercreator_character 
WHERE character_id < 80 
AND character_id > 50;
```

### Use "BETWEEN" to simplify complex conditional statements

```SQL
SELECT character_id,name
FROM charactercreator_character 
WHERE character_id BETWEEN 10 and 20;
```

### Comment out a line with two dashes `--`

```SQL
SELECT character_id,name
FROM charactercreator_character 
--WHERE character_id BETWEEN 10 and 20;
```

### use GROUPBY to select groups of records that have the same value

We need to provide a function (like COUNT()) for the query to do to each unique group.

```SQL
SELECT name,COUNT(*)
FROM charactercreator_character
GROUP BY name;
```

### Sort the query by count

```SQL
SELECT name,COUNT(*)
FROM charactercreator_character
GROUP BY name
ORDER BY COUNT(*);
```

### Sort in ascending order

```SQL
SELECT name,COUNT(*)
FROM charactercreator_character
GROUP BY name
ORDER BY COUNT(*) ASC;
```

### Sort in descending order

```SQL
SELECT name,COUNT(*)
FROM charactercreator_character
GROUP BY name
ORDER BY COUNT(*) DESC;
```

## Sort by alphabetical order

```SQL
SELECT name,COUNT(*)
FROM charactercreator_character
GROUP BY name
ORDER BY name;
```

You can also indicate ascending and descending when sorting alphabetically. `DESC` will give you reverse-alphabetical order.

### Get names of characters that are duplicates

```SQL
SELECT name,COUNT(*)
FROM charactercreator_character
GROUP BY name
ORDER BY COUNT(*) DESC
WHERE COUNT(*)>1;
```

### Use an alias to refer to a selection

```SQL
SELECT name,COUNT(*) as total_name_repeated
FROM charactercreator_character
GROUP BY name
ORDER BY total_name_repeated DESC
WHERE total_name_repeated>1;
```

Notice that when we use an alias, the column header of our attribute is renamed to have the alias as the column header.
