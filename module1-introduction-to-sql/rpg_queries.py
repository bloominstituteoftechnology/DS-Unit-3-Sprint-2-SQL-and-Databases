"""
----------------------------------------------------------------
             RPG DataBase Queries
----------------------------------------------------------------
"""
import sqlite3


# ___ instantiate and return connection obj _________
def conx_sqlite(db):
    cnx = sqlite3.connect(db)
    return cnx


# ___ QUERIES _________________________________
def run_queries(c):
    # _____ How Many Characters_____________________
    for row in c.execute('SELECT COUNT(character_id) FROM charactercreator_character'):
        print('There are a total of', row[0], 'Characters')

    # _____ How many Character Types _____________
    for row in c.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'):
        print(row[0], 'Clerics')
    for row in c.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'):
        print(row[0], 'Fighters')
    for row in c.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_mage'):
        print(row[0], 'Mages')
    for row in c.execute('SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer'):
        print(row[0], 'Necromancers')
    for row in c.execute('SELECT COUNT(character_ptr_id) FROM charactercreator_thief'):
        print(row[0], 'Thieves')
    print()

    # _______________ How many Items _________________________________
    for i in c.execute('SELECT COUNT(item_id) FROM armory_item'):
        print('There are a total of', i[0], 'items')
    for w in c.execute('SELECT COUNT(item_ptr_id) FROM armory_weapon'):
        print(w[0], 'Weapons')
    print((i[0] - w[0]), 'Non-Weapons')
    print()

    query1 = '''
    SELECT AVG(items)
    FROM (
        SELECT character_id, count(item_id) as items
        FROM charactercreator_character_inventory
        GROUP BY character_id);
    '''
    for i in c.execute(query1):
        print('Each character has average of', i[0], 'items')

    # _______________________________________________________________________
    '''
    How many Items does each character have? (Return first 20 rows)
    How many Weapons does each character have? (Return first 20 rows)
    On average, how many Items does each Character have?
    On average, how many Weapons does each character have?
    '''
    # for row in c.execute('SELECT * FROM armory_item ORDER BY name'):
    #        print(row)

    return


def main():
    conn = conx_sqlite('rpg_db.sqlite3')
    cur = conn.cursor()  # create cursor
    run_queries(cur)
    cur.close()
    conn.close()   # Close the connection
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
