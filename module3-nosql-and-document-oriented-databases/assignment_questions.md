
## How was working with MongoDB different from working with PostgreSQL?
Working with MongoDB was different in that creating tables and inserting data into those tables was different. For PostgreSQL, you use SQL to create tables.

`(ex. CREATE TABLE (col1 dtype, col2 dtype, col3 dtype))`

For MongoDB, tables are called Collections, and its rows are called document. To create a table in MongoDB, you would:

`db.table_name`

And adding documents (rows) would be:

`db.table_name.insert_one()`

For MongoDB, in order to insert data, it really needs to be a 'dict' type or 'JSON' type.


## What was easier, and what was harder?"
I found it easier to create a database and tables in MongoDB. Although I found it slightly harder to get the data into the right format in order to insert it into the tables. 