#!/usr/bin/env python

import psycopg2
import sqlite3
from psycopg2 import sql


def sqlite_to_psql(sqlite_connection, psql_connection):
	# Get the tables from sqlite
	query = """
		SELECT name, sql
		FROM sqlite_master
		WHERE type = 'table'
			AND (name LIKE 'character%'
				OR name LIKE 'armory%')
		ORDER BY name ASC;
	"""
	curr = sqlite_connection.cursor()
	curr.execute(query)
	results = curr.fetchall()
	curr.close()

	# Build the tables in Postgres
	curr = psql_connection.cursor()
	tables = []
	for row in results:
		table = row[0]
		tables.append(table)
		print(f'Building table {table}...')

		delete_query = sql.SQL("""
			DROP TABLE IF EXISTS {} CASCADE;
		""").format(sql.Identifier(table))
		create_query = row[1].replace('AUTOINCREMENT', '').replace('bool', 'smallint')

		curr.execute(delete_query)
		curr.execute(create_query)
	curr.close()
	print('Committing changes.')
	psql_connection.commit()

	for table in tables:
		print(f'Filling table {table}...')
		# This is unsafe but I'm lazy
		query = f"""
		SELECT * FROM {table};
		"""
		curr = sqlite_connection.cursor()
		curr.execute(query)
		values = curr.fetchall()
		curr.close()

		# Build the query with the correct number of value placeholders
		values_placeholder = ('%s,' * len(values[0])).rstrip(',')
		fill_query = sql.SQL("""
			INSERT INTO {} VALUES (%(pholder)s);
		""" % {'pholder': values_placeholder}
		).format(sql.Identifier(table))
		curr = psql_connection.cursor()
		curr.executemany(fill_query, values)
		curr.close()
	print('Committing changes.')
	psql_connection.commit()
	print('Done.')


if __name__ == "__main__":
	with psycopg2.connect(database="lambda_module1") as psql_conn:
		with sqlite3.connect('./module1-introduction-to-sql/rpg_db.sqlite3') as sqlite_conn:
			sqlite_to_psql(sqlite_conn, psql_conn)


