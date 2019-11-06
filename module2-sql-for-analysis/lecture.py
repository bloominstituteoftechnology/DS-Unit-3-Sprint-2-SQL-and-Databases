#!/usr/bin/env python

import psycopg2

query = """
	CREATE TABLE IF NOT EXISTS charactercreator_character (
		character_id SERIAL PRIMARY KEY NOT NULL,
		name VARCHAR(30) NOT NULL,
		level INT NOT NULL,
		exp INT NOT NULL,
		hp INT NOT NULL,
		strength INT NOT NULL,
		intelligence INT NOT NULL,
		dexterity INT NOT NULL,
		wisdom INT NOT NULL
	);
"""

if __name__ == "__main__":
	with psycopg2.connect(database="lambda_module1") as conn:
		curr = conn.cursor()
		curr.execute(query)
		curr.close()
		conn.commit()

		curr = conn.cursor()
		query = 'SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = \'charactercreator_character\';'
		curr.execute(query)
		print(curr.fetchall())
		curr.close()


