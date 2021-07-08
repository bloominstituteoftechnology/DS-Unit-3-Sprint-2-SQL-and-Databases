#! usr/bin/env python3
import sqlite3
import pandas as pd


if __name__ == '__main__':
  # Open a connection to a new (blank) database
  conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
  curs = conn.cursor()

  # Instantiate a DataFrame
  df = pd.read_csv('buddymove_holidayiq.csv')

  # Use df.to_sql to insert the data into a new table review in the SQLite3 database
  df.to_sql('review', con=conn)

  print('Count how many rows you have - it should be 249!')
  print(curs.execute('SELECT COUNT(*) FROM review;').fetchall())

  print('How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
  print(curs.execute('SELECT COUNT(*) FROM review WHERE Nature > 100 and Shopping > 100;').fetchall())

  print('(Stretch) What are the average number of reviews for each category?')
  print(curs.execute('SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM review;').fetchall())
