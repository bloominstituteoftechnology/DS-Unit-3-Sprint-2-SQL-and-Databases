"""Testing SQL queries to find info"""

import sqlite3

conn = sqlite3.connect('/Users/FluffyBear/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()

get_table = 'SELECT * FROM charactercreator_character LIMIT 10'

get_columns = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS"
# WHERE TABLE_NAME = N'charactercreator_character'"

print(curs.execute(get_columns).fetchall())
