#!/usr/bin/env python

import pymongo
import sqlite3


#############################################################
# "How was working with MongoDB different from working with #
# PostgreSQL? What was easier, and what was harder?"        #
#                                                           #
# Working with MongoDB wasn't particularly different from   #
# working with PostgreSQL. MongoDB felt "flimsier" - the    #
# lack of a schema would make me dubious of any data I      #
# retrieve from the database, as there is no protection     #
# against invalid data types, duplicate IDs, etc.           #
#############################################################


def sqlite_to_mongodb(sqlite_connection, mongo_db):
	print('Loading data from sqlite...')
	# Get the tables from sqlite
	query = """
		SELECT name
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
	# Get the tables
	tables = [row[0] for row in results]
	print(f'Found tables: {tables}')

	for table in tables:
		print(f'Dropping collection {table}...')
		mongo_db[table].drop()

		print(f'Transferring table {table} to collection {table}...')
		query = f"""
			SELECT * FROM {table};
		"""
		curr = sqlite_connection.cursor()
		curr.execute(query)
		results = curr.fetchall()
		description = curr.description
		curr.close()

		results_dicts = []
		for row in results:
			result_dict = dict(zip([coltup[0] for coltup in curr.description], row))
			results_dicts.append(result_dict)

		mongo_db[table].insert_many(results_dicts)

	print('Done.')


if __name__ == "__main__":
	with sqlite3.connect('./module1-introduction-to-sql/rpg_db.sqlite3') as sqlite_conn:
		with open('./module3-nosql-and-document-oriented-databases/mongodb-password', 'r') as pwfile:
			PASSWORD = pwfile.read()

		url = f'mongodb+srv://dbadmin:{PASSWORD}@c0-wudpf.azure.mongodb.net/test?retryWrites=true&w=majority'
		client = pymongo.MongoClient(url)

		try:
			client.admin.command('ismaster')
			db = client.get_default_database()
			sqlite_to_mongodb(sqlite_conn, db)
		finally:
			client.close()


