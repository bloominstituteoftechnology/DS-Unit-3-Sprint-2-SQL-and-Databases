## Assignment - Part 1, Querying a Database

This directory contains a file `rpg_db.sqlite3`, a database for a hypothetical
role-playing game. This test data has dozens-to-hundreds of randomly
generated characters with various tables holding information about these characters. Also generated are Items, Weapons, and
connections between these generated characters. Note that, while the name field was
randomized, the numeric and boolean fields were left as defaults.

Use `sqlite3` to load and write queries to explore the data, and answer the
following questions. You should store each query as a string and label each
as the indicated variable names. Also, store each of these queries in a seperate 
file named `queries.py` and either run these queries in the file or import them 
into another: 

- `TOTAL_CHARACTERS`: How many total Characters are there?
- `TOTAL_SUBCLASS`: How many of each specific subclass (the `necromancer` table)?
- `TOTAL_ITEMS`: How many total Items?
- `WEAPONS`: How many of the Items are weapons? 
- `NON_WEAPONS`: How many of the items are not weapons?
- `CHARACTER_ITEMS`: How many Items does each character have? (Return first 20 rows)
- `CHARACTER_WEAPONS`: How many Weapons does each character have? (Return first 20 rows)
- `AVG_CHARACTER_ITEMS`: On average, how many Items does each Character have?
- `AVG_CHARACTER_WEAPONS`: On average, how many Weapons does each character have?

You do not need all the tables - in particular, the `account_*`, `auth_*`,
`django_*`, and `socialaccount_*` tables are for the application and do not have
the data you need. the `charactercreator_*` and `armory_*` tables and where you
should focus your attention. `armory_item` and `charactercreator_character` are
the main tables for Items and Characters respectively - the other tables are
subsets of them by type (i.e. subclasses), connected via a key (`item_id` and
`character_id`).

You can use the DB Browser or other tools to explore the data and work on your
queries if you wish, but to complete the assignment you should write a file
`rpg_queries.py` that imports `sqlite3` and programmatically executes and
reports results for the above queries.

Some of these queries are challenging - that's OK! You can keep working on them
tomorrow as well (we'll visit loading the same data into PostgreSQL). It's also
OK to figure out the results partially with a query and partially with a bit of
logic or math afterwards, though doing things purely with SQL is a good goal.
[Subqueries](https://www.w3resource.com/sql/subqueries/understanding-sql-subqueries.php)
and [aggregation functions](https://www.sqltutorial.org/sql-aggregate-functions/)
may be helpful for putting together more complicated queries.

## Assigment - Part 2, Making and populating a Database

Load the data (use `pandas`) from the provided file `buddymove_holidayiq.csv`
(the [BuddyMove Data
Set](https://archive.ics.uci.edu/ml/datasets/BuddyMove+Data+Set)) - you should
have 249 rows, 7 columns, and no missing values. The data reflects the number of
place reviews by given users across a variety of categories (sports, parks,
malls, etc.).

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `buddymove_holidayiq.sqlite3`
- Use `df.to_sql`
  ([documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html))
  to insert the data into a new table `review` in the SQLite3 database

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 249!
- How many users who reviewed at least 100 `Nature` in the category also
  reviewed at least 100 in the `Shopping` category?
- **Stretch Goal** What are the average number of reviews for each category?

Your code (to reproduce all above steps) should be saved in
`buddymove_holidayiq.py`. 

When you submit your files to Canvas you should upload `queries.py`, 
`buddymove_holidayiq.py`, and `buddymove_holidayiq.sqlite3`.