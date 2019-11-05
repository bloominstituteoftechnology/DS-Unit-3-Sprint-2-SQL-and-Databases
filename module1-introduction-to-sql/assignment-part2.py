#!/usr/bin/env python

import sqlite3
import pandas


df = pandas.read_csv('./module1-introduction-to-sql/buddymove_holidayiq.csv')
with sqlite3.connect('./module1-introduction-to-sql/buddymove_holidayiq.sqlite3') as conn:
	df.to_sql('review', conn, if_exists='replace')

	curr = conn.cursor()

	query = '''
		SELECT COUNT(*) FROM review
		'''
	curr.execute(query)
	result = curr.fetchone()[0]
	print(f'review has {result} rows.')

	query = '''
		SELECT COUNT(DISTINCT `User Id`) FROM review
		WHERE Nature >= 100 AND Shopping >= 100
		'''
	curr.execute(query)
	result = curr.fetchone()[0]
	print(f'review has {result} users that reviewed at least 100 in both Nature and Shopping')

	query = '''
		SELECT AVG(Sports) AS Sports,
			AVG(Religious) AS Religious,
			AVG(Nature) AS Nature,
			AVG(Theatre) AS Theatre,
			AVG(Shopping) AS Shopping,
			AVG(Picnic) AS Picnic
		FROM review
		'''
	curr.execute(query)
	results = curr.fetchone()
	result_dict = dict(zip([coltup[0] for coltup in curr.description], results))
	for column, value in result_dict.items():
		print(f'{column} had an average of {value} reviews.')

	curr.close()

