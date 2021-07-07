import sqlite3
import pandas as pd

class Quering():
    '''
    Quering through rpg_dp.sqlite3
    '''

    def __init__(self):
        self.self = self


    def character_cnt(self):
        '''
        #1 How many total Characters are there?
        '''
        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        char_cnt = curs.execute("""SELECT COUNT(DISTINCT(character_id))
                                FROM charactercreator_character;""")
        
        char_cnt_result = curs.fetchone()
        print(f'There are total characters', char_cnt_result)

        conn.close()


    def characters_in_subclass(self):
        '''
        #2 How many of each specific subclass?
        '''
        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        subclass_char = curs.execute(
                        """SELECT 'mages', COUNT(*) 
                        FROM charactercreator_mage 
                        
                        UNION
                                            
                        SELECT 'clerics', COUNT(*) 
                        FROM charactercreator_cleric

                        UNION

                        SELECT 'fighter', COUNT(*) 
                        FROM charactercreator_fighter

                        UNION

                        SELECT 'thieves', COUNT(*) 
                        FROM charactercreator_thief
                        
                        UNION
                        
                        SELECT 'necromancer', COUNT(*)
                        FROM charactercreator_necromancer;""")

        subclass_cnt = curs.fetchall()
        print(f'Number of characters in each subclass:\n', subclass_cnt)

        conn.close()

    def total_items(self):
        '''
        "#3 How many total Items?"
        '''

        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        items = curs.execute("""SELECT COUNT(item_id)
                             FROM armory_item""")

        items_total = curs.fetchall()

        print(f'Total {items_total[0]}')

        conn.close()

    def weapons_not_weapons(self):
        '''
        "#4 How many of the Items are weapons? How many are not?"
        '''
        conn = sqlite3.connect('rpg_dg.sqlite3')
        curs = conn.cursor()
        weapon_cnt = """SELECT COUNT(item_ptr_id)
                    FROM armory_weapon"""
        weapons = curs.fetchone()

        not_weapon_cnt = curs.execute(
                        """SELECT COUNT(item_id)
                        FROM armory_item
                        WHERE NOT EXISTS 
                            (SELECT item_ptr_id
                            FROM armory_weapon 
                            WHERE armory_weapon.item_ptr_id = armory_item.item_id;""")
        not_weapons = curs.fetchone()

        print("{weapons[0]} weapons and {not_weapons[0]} not weapons." )

        conn.close()

    def items_per_character(self):
        """
        #5 How many Items does each character have? 
        (Return first 20 rows)
        """
        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        items_per_char = curs.execute("""SELECT character_id, COUNT(item_id)
                                      FROM charactercreator_character_inventory
                                      GROUP BY character_id
                                      LIMIT 20;""")
        items_char = curs.fetchall()
        print("Items per charachter (first 20):\n", items_char)
        
        conn.close()
    
    def weapons_per_character(self):
        """
        #6 How many Weapons does each character have? 
        (Return first 20 rows)
        """
        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        weapons_each = curs.execute("""SELECT COUNT(item_id)
                                    FROM charactercreator_character_inventory inventory
                                    JOIN armory_weapon as weapon
                                    ON weapon.item_ptr_id = inventory.item_id
                                    GROUP BY character_id;""")
        
        weapons_per_char = curs.fetchall()

        print('Number of weapons per character:\n', weapons_per_char)

        conn.close()

    
    def avg_items(self):
        """
        #7 On average, how many Items does each Character have?
        """

        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        average_items = curs.execute("""SELECT AVG(num_items)
                                     FROM(SELECT character_id, COUNT(item_id) as num_items
                                     FROM charactercreator_character_inventory
                                     GROUP BY character_id) AS grouped;""")

        avg_items_char = curs.fetchall()

        print(f'The average number of items per character is {avg_items_char}')

        conn.close()


    def avg_weapons(self):
        """
        #8 On average, how many Weapons does each character have
        """
        conn = sqlite3.connect('rpg_db.sqlite3')
        curs = conn.cursor()

        average_weapons = curs.execute("""SELECT AVG(weapon_items)
                                        FROM(SELECT character_id, COUNT(item_id) as weapon_items
                                        FROM charactercreator_character_inventory
                                        WHERE EXISTS 
                                            (SELECT item_ptr_id
                                            FROM armory_weapon 
                                            WHERE armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id)
                                        GROUP BY character_id);""")

        avg_weap = curs.fetchall()

        print(f'The average number of weapons per character is {avg_weap}')

        conn.close()