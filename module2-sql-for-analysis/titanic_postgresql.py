"""
Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
thinking about the schema to make sure it is appropriate for the columns.
[Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
be useful. Once it is set up, write a `insert_titanic.py` script that uses
`psycopg2` to connect to and upload the data from the csv, and add the file to
your repo. Then start writing PostgreSQL queries to explore the data!
"""

import psycopg2
import sqlite3
