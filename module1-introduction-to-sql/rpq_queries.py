import sqlite3
import pandas as pd


class QueryRPGDB:
    def __init__(self):
        self.self = self

    def chara_count(self):
        connection = sqlite3.connect('rpg_db.sqlite3')

        cursor = connection.cursor()
        cursor.execute("""SELECT COUNT (DISTINCT character_id) FROM charactercreator_character""")

        print('Querying total character amounts:', cursor.fetchone())

        connection.close()

    def subclass_count(self):
        connection = sqlite3.connect('rpg_db.sqlite3')

        cursor = connection.cursor()
        cursor.execute("""SELECT 
                (SELECT COUNT(*) FROM charactercreator_cleric) AS Clerics,
                (SELECT COUNT(*) FROM charactercreator_fighter) AS Fighters,
                (SELECT COUNT(*) FROM  charactercreator_mage) AS Mages,
                (SELECT COUNT(*) FROM  charactercreator_thief) AS Thieves,
                (SELECT COUNT(*) FROM  charactercreator_necromancer) AS Necromancers""")

        names = list(map(lambda x: x[0], cursor.description))
        subclass_counts = cursor.fetchall()
        pretty_results = pd.DataFrame(subclass_counts, columns=names)

        print(pretty_results)

        connection.close()


db_connect = QueryRPGDB()
db_connect.chara_count()
db_connect.subclass_count()
