import sqlite3
import pandas as pd
conn = sqlite3.connect('../rpg_db.sqlite3')


####### HOW MANY TOTAL CHARACTERS ARE THERE? #######
c = conn.cursor()
c.execute(' SELECT COUNT(character_id) FROM charactercreator_character ; ')
print(f'\n\nThere are {c.fetchone()[0]} total characters in this database:')


####### HOW MANY SUBCLASS PLAYERS? #######
c = conn.cursor()
query = '''
        select( SELECT COUNT(character_ptr_id) FROM charactercreator_mage ) ,
              ( SELECT COUNT(character_ptr_id) FROM charactercreator_thief ) ,
              ( SELECT COUNT(character_ptr_id) FROM charactercreator_fighter ) ,
              ( SELECT COUNT(character_ptr_id) FROM charactercreator_cleric ) ;
        '''
c.execute(query)
mage, thief, fighter, cleric = c.fetchone()
print(f'{mage} mages\n{thief} thiefs\n{fighter} fighters\n{cleric} clerics\n\n')


####### HOW MANY ITEMS? #######
c = conn.cursor()
query = '''
            SELECT
                COUNT(item_id)
            FROM
                armory_item
        '''
c.execute(query)
total_items = c.fetchone()[0]
print(f'There are {total_items} items in the database:')


####### HOW MANY WEAPONS VS NOT WEAPONS #######
c = conn.cursor()
query = ' SELECT COUNT(item_ptr_id) FROM armory_weapon ; '
c.execute(query)
weapons = c.fetchone()[0]
print(f'{weapons} - weapons\n{total_items-weapons} - not weapons\n\n')


####### HOW MANY ITEMS DO THE FIRST 20 HAVE #######
c = conn.cursor()

query = '''
            SELECT
                cc.character_id cid,
            COUNT
                (charactercreator_character_inventory.item_id) AS NumOfItems
            FROM
                charactercreator_character as cc
            LEFT JOIN
                charactercreator_character_inventory
            ON
                cid = charactercreator_character_inventory.character_id
            GROUP BY
                cid
            LIMIT
                20;
        '''
c.execute(query)
df = pd.DataFrame(c.fetchall(),columns=['Character ID','Number of Items'])
print('How many items do the first 20 players have?\n', df.head(20), '\n\n')


####### HOW MANY WEAPONS DO THE FIRST 20 HAVE #######
c = conn.cursor()

query = '''
            SELECT 
                cc.character_id cid,
                COUNT( cci.item_id )
            FROM
                charactercreator_character cc,
                charactercreator_character_inventory cci
            WHERE
                cci.item_id in ( SELECT 
                                aw.item_ptr_id weaponid 
                            FROM
                                armory_weapon aw
                            )
            GROUP BY
                cid
            LIMIT
                20
        '''
c.execute(query)
df = pd.DataFrame(c.fetchall(),columns=['Character ID','Number Of Weapons'])
print('How many Weapons do the first 20 players have?\n', df.head(20), '\n\n')


####### HOW MANY ITEMS AVG DO THEY HAVE #######
c = conn.cursor()

query = '''
            SELECT
            AVG( NumOfItems )
            FROM ( 
                    SELECT
                        cc.character_id cid,
                        COUNT
                            (charactercreator_character_inventory.item_id) AS NumOfItems
                    FROM
                        charactercreator_character as cc
                    LEFT JOIN
                        charactercreator_character_inventory
                    ON
                        cid = charactercreator_character_inventory.character_id
                    GROUP BY
                        cid
             )
        '''
c.execute(query)
print(f'Average Number of Items: {c.fetchone()[0]}')
