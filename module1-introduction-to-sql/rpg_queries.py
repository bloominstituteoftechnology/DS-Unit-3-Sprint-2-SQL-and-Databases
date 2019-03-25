import sqlite3


def start_connection(db):
    '''End SQL database connection'''
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    return cursor

def query_database(db):
    '''query SQL database'''

    cursor = start_connection(db)

    # How many total Characters are there?
    query = 'SELECT COUNT(character_id) FROM charactercreator_character'
    for row in cursor.execute(query).fetchall():
        print(row[0], 'Characters')

    # - How many of each specific subclass?
    query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'
    for row in cursor.execute(query):
        print(row[0], 'Clerics')
    query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'
    for row in cursor.execute(query):
        print(row[0], 'Fighters')
    query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage'
    for row in cursor.execute(query):
        print(row[0], 'Mage')
    query = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer'
    for row in cursor.execute(query):
        print(row[0], 'Necromancer')
    query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief'
    for row in cursor.execute(query):
        print(row[0], 'Thief')

    # - How many total Items?
    query = 'SELECT COUNT(item_id) FROM armory_item'
    for row in cursor.execute(query):
        print(row[0], 'items')    

    # - How many of the Items are weapons? How many are not?
    query = 'SELECT COUNT(item_ptr_id) FROM armory_weapon'
    for row2 in cursor.execute(query):
        print(row2[0], 'weapons')
    print(row[0] - row2[0], 'Non-Weapons')

    # - How many Items does each character have? (Return first 20 rows)
    query = '''
        SELECT character_id, COUNT(item_id) as item_count
        FROM charactercreator_character_inventory
        GROUP BY character_id
        LIMIT 20
    '''
    for row in cursor.execute(query):
        print(row[0],':' ,row[1])

    # - How many Weapons does each character have? (Return first 20 rows)
    query = '''
        SELECT character_id, COUNT(item_id) as weapon_count
        FROM charactercreator_character_inventory
        WHERE item_id IN (SELECT distinct item_ptr_id
                        FROM armory_weapon)
        GROUP BY character_id
        LIMIT 20
    '''
    for row in cursor.execute(query):
        print(row[0],':' ,row[1])

    # - On average, how many Items does each Character have?
    query = '''
        SELECT AVG(items) as average_items
            FROM (
                SELECT character_id, COUNT(item_id) as items
                FROM charactercreator_character_inventory
                GROUP BY character_id
            )
    '''
    for row in cursor.execute(query):
        print(row[0], 'average items per character')

    # - On average, how many Weapons does each character have?
    query = '''
        SELECT AVG(items) as average_weapons
            FROM (
                SELECT character_id, COUNT(item_id) as items
                FROM charactercreator_character_inventory
                WHERE item_id IN (SELECT distinct item_ptr_id
                        FROM armory_weapon)
                GROUP BY character_id
            )
    '''
    for row in cursor.execute(query):
        print(row[0], 'average weapons per character')

def main():
    db = 'rpg_db.sqlite3'
    query_database(db)

if __name__ == '__main__':
    main()