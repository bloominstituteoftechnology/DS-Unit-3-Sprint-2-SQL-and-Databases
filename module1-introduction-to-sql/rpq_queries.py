import sqlite3
import pandas as pd


class QueryRPGDB:
    """
    Class for querying rpg_db
    """
    def __init__(self):
        self.self = self

    def chara_count(self):
        """
        Queries for unique values id values in charactercreator_character temple table
        :return:
        """
        connection = sqlite3.connect('rpg_db.sqlite3')

        cursor = connection.cursor()
        total_chara_counts = cursor.execute("""SELECT COUNT (DISTINCT character_id) FROM charactercreator_character""")

        pretty_results = pd.DataFrame(total_chara_counts, columns=['Total_Character_Count'])

        print(pretty_results)

        connection.close()

    def subclass_count(self):
        """
        Queries multiple character_creator subclasses for counts, maps column names to table what we named the separate
        counts
        :return:
        """
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

    def item_total_weapon_distinguish(self):
        """
        Queries DB for total items in item table and queries for matching weapon id in item table
        :return:
        """
        connection = sqlite3.connect('rpg_db.sqlite3')

        cursor = connection.cursor()

        total_item_query = cursor.execute("""SELECT COUNT (DISTINCT item_id) FROM armory_item""")
        total_item_counts = total_item_query.fetchone()

        total_weapon_query = cursor.execute("""SELECT COUNT(*) 
        FROM armory_item, armory_weapon WHERE armory_item.item_id = armory_weapon.item_ptr_id""")

        total_weapon_counts = total_weapon_query.fetchone()

        total_non_weapon_query = cursor.execute("""SELECT COUNT(*) 
        FROM armory_item WHERE item_id NOT IN(SELECT item_ptr_id FROM armory_weapon)""")

        total_non_weapon_counts = total_non_weapon_query.fetchone()

        # this tricky list extracts the data from the sqlite3 queried tuple so we can pass them in as 1x2 instead of 2x1
        counts = [total_item_counts[0], total_weapon_counts[0], total_non_weapon_counts[0]]

        pretty_results = pd.DataFrame([counts], columns=['Total_Items_Count', 'Items_Are_Weapons', 'Items_Not_Weapons'])

        print(pretty_results)

        connection.close()

    def character_items(self, default_rows=20):
        """

        :param default_rows: Number of rows to return from query: default 20
        :return:
        """
        connection = sqlite3.connect('rpg_db.sqlite3')

        cursor = connection.cursor()

        # this group by statement will return a tuple of the selected values
        # it is very hard to work with out of the box, especially if you want it in a data frame
        owned_item_by_char = cursor.execute("""SELECT DISTINCT character_id, COUNT(character_id) 
        FROM charactercreator_character_inventory GROUP BY character_id""")

        owned_item_result = owned_item_by_char.fetchmany(default_rows)

        # processing for tuple
        tuple1, tuple2 = zip(*owned_item_result)

        list1 = list(tuple1)
        list2 = list(tuple2)

        series1 = pd.Series(list1)
        series2 = pd.Series(list2)

        # the only way I could get this to work was to map with dictionary, otherwise you get a 2 row
        # dataframe with each row holding a single list of 20 values...
        pretty_results = pd.DataFrame(({'Character_ID': series1, 'Items_Owned': series2}))

        print(pretty_results)

    def weapons_owned_query(self, default_rows=20):

        connection = sqlite3.connect('rpg_db.sqlite3')
        cursor = connection.cursor()

        owned_weapons_query = cursor.execute("""
        SELECT DISTINCT charactercreator_character_inventory.character_id AS CHARACTER_ID,
        count(charactercreator_character_inventory.character_id) AS OWNED_WEAPONS
        
        FROM charactercreator_character_inventory, armory_weapon
        
        WHERE armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
        
        GROUP BY charactercreator_character_inventory.character_id
        """)

        owned_item_result = owned_weapons_query.fetchmany(default_rows)


        # processing for tuple
        tuple1, tuple2 = zip(*owned_item_result)

        list1 = list(tuple1)
        list2 = list(tuple2)

        series1 = pd.Series(list1)
        series2 = pd.Series(list2)

        # the only way I could get this to work was to map with dictionary, otherwise you get a 2 row
        # dataframe with each row holding a single list of 20 values...
        pretty_results = pd.DataFrame(({'Character_ID': series1, 'Weapons_Owned': series2}))

        print(pretty_results)


db_connect = QueryRPGDB()
db_connect.chara_count()
db_connect.subclass_count()
db_connect.item_total_weapon_distinguish()
db_connect.character_items()
db_connect.weapons_owned_query()
