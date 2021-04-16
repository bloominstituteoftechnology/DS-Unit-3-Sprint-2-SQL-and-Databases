#!/usr/bin/env python

import pymongo


def verify(mongo_db):
	collection = mongo_db['charactercreator_character']
	chars_lt_5 = collection.find({'character_id': {'$lt': 5}})
	for char in chars_lt_5:
		print(char)


if __name__ == '__main__':
	with open('./module3-nosql-and-document-oriented-databases/mongodb-password', 'r') as pwfile:
		PASSWORD = pwfile.read()

	url = f'mongodb+srv://dbadmin:{PASSWORD}@c0-wudpf.azure.mongodb.net/test?retryWrites=true&w=majority'
	client = pymongo.MongoClient(url)

	try:
		client.admin.command('ismaster')
		db = client.get_default_database()
		verify(db)
	finally:
		client.close()
