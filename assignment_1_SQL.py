# Assignment 1 for SQL 
"""A series of SQL queries to figure out answer to the 
rpq_db"""
import sqlite3


def main():
	conn = sqlite3.connect('rpg_db.sqlite3')
	c = conn.cursor()

	query_1 = """SELECT * FROM charactercreator_character AS character"""

	c.execute(query_1)
	
	c.fetchall()
main()






