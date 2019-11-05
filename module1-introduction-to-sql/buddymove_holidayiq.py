"""
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
- (*Stretch*) What are the average number of reviews for each category?

Your code (to reproduce all above steps) should be saved in
`buddymove_holidayiq.py`, and added to the repository along with the generated
SQLite database.
"""

import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('buddymove_holidayiq', con=conn)
conn.execute("SELECT * FROM buddymove_holidayiq;").fetchone()

query_total_rows = """
	SELECT COUNT(*)
	FROM buddymove_holidayiq;
	"""
total_rows = conn.execute(query_total_rows).fetchone()[0]
print("The total rows in buddymove_holidayiq is {}".format(total_rows))

query_reviewed = """
	SELECT COUNT(*)
	FROM buddymove_holidayiq
	WHERE Nature > 100 
	AND Shopping > 100;
	"""
reviewed = conn.execute(query_reviewed).fetchone()[0]
print("The total rows in buddymove_holidayiq where Shopping and",
	"Nature is more than 100 is {}"
	.format(reviewed))
