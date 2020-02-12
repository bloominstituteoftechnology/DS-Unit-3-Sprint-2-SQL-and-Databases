import sqlite3
import os

# loaded database file name
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(BASE_DIR, "rpg_db.sqlite3")

"""
db_file = os.path.join(os.path.dirname(__file__),
              "..", "rpg_db.sqlite3")
"""

def create_connection(db_file):
  """Create a database connection to SQLite specified by db_file"""
  conn = None

  try: 
      conn = sqlite3.connect(db_file)
  except sqlite3.Error as e:
        print ("Error in connection", e)
    
  return conn

def get_character_count(conn):
  """Queary database to get character count"""
  cur = conn.cursor()
  cur.execute(
    """
    SELECT COUNT(DISTINCT character_id)
    FROM charactercreator_character
    """
  )

  return cur.fetchall()[0][0]

def get_subclass_count(conn):
  """Queary database to get subclass count"""
  cur = conn.cursor()
  
  # Dictionary with keys to hold count values returned by query 
  subclasses = {'mage': 0, 'cleric': 0, 
                'fighter': 0, 'thief': 0}

  for sub in subclasses:
  # Loop through query using keys representing classes in varying tables  

    cur.execute(
      """
      SELECT COUNT(DISTINCT charactercreator_"""+sub+""".character_ptr_id)
      FROM charactercreator_"""+sub
      )
    subclasses[sub] = cur.fetchall()[0][0]
  
  return subclasses

def get_item_count(conn):
  """Queary database to get item count"""
  cur = conn.cursor()
  cur.execute(
    """
    SELECT COUNT(DISTINCT item_id)
    FROM armory_item
    """
  )

  return cur.fetchall()[0][0]

def get_weapon_count(conn):
  """Queary database to get weapon vs non-weapon count"""
  cur = conn.cursor()
  
  # Dictionary with keys to hold count values returned by query 
  items = {'weapon': 0, 'non_weapon': 0}

  cur.execute(
    """
    SELECT

      CASE
      WHEN armory_weapon.item_ptr_id is not null THEN 'weapon'
      ELSE 'non-weapon'
      END AS weapon_type,
      count(armory_item.item_id)
      
    FROM armory_item
    LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id = armory_item.item_id
    GROUP BY weapon_type
    """
    )
  
  table = cur.fetchall()
  items['weapon'] = table[0][1]
  items['non_weapon'] = table[1][1]
  
  return items

def get_item_count_per_character(conn):
  """Queary database to get item count for each character(first 20 rows)"""
  cur = conn.cursor()
  cur.execute(
    """
    SELECT charactercreator_character.character_id,
            COUNT(armory_item.item_id)
    FROM charactercreator_character
    JOIN charactercreator_character_inventory 
      ON charactercreator_character_inventory.character_id 
      = charactercreator_character.character_id
    JOIN armory_item ON charactercreator_character_inventory.item_id
      = armory_item.item_id
    GROUP BY armory_item.item_id
    LIMIT 20
    """
  )
  
  return cur.fetchall()

def get_weapon_count_per_character(conn):
  """Queary database to get weapon count for each character(first 20 rows)"""
  cur = conn.cursor()
  cur.execute(
    """
    SELECT charactercreator_character.character_id,
        count(armory_weapon.item_ptr_id) as weapons
    FROM charactercreator_character
    JOIN charactercreator_character_inventory 
      ON charactercreator_character_inventory.character_id 
      = charactercreator_character.character_id
    JOIN armory_item ON charactercreator_character_inventory.item_id
      = armory_item.item_id
    JOIN armory_weapon ON armory_weapon.item_ptr_id = armory_item.item_id
    GROUP BY charactercreator_character.character_id
    LIMIT 20
    """
  )
  
  return cur.fetchall()

def get_item_avg(conn):
  """Queary database to get average number of items per character"""
  cur = conn.cursor()
  cur.execute(
    """
    SELECT AVG(item_count.items)
    FROM(

      SELECT COUNT(armory_item.item_id) AS items
      FROM charactercreator_character
      JOIN charactercreator_character_inventory 
        ON charactercreator_character_inventory.character_id 
        = charactercreator_character.character_id
      JOIN armory_item ON charactercreator_character_inventory.item_id
        = armory_item.item_id
      GROUP BY charactercreator_character.character_id
      
    )item_count
    """
  )
  
  return cur.fetchall()[0][0]

def get_weapon_avg(conn):
  """Queary database to get average number of weapons per character"""
  cur = conn.cursor()
  cur.execute(
    """
    SELECT AVG(weapon_count.weapons)
    FROM(

      SELECT COUNT(armory_weapon.item_ptr_id) AS weapons
      FROM charactercreator_character
      JOIN charactercreator_character_inventory 
        ON charactercreator_character_inventory.character_id 
        = charactercreator_character.character_id
      JOIN armory_item ON charactercreator_character_inventory.item_id
        = armory_item.item_id
      JOIN armory_weapon ON armory_weapon.item_ptr_id = armory_item.item_id
      GROUP BY charactercreator_character.character_id
      
    )weapon_count
    """
  )
  
  return cur.fetchall()[0][0]


def main():
  """Print all results from queries"""

  # start a connection to database. To be used Globably
  CONN = create_connection(db_file)

  # Character Counts
  character_count = get_character_count(CONN)
  print(f"There are {character_count} characters in the character")

  # Subclass Totals
  subs = get_subclass_count(CONN)
  for k,v in subs.items():
    print(f'{k} : {v}')
  print (f'Total : {sum(subs.values())}')

  # Items Counts
  item_count = get_item_count(CONN)
  print(f"There are {item_count} items in the armory table")

  # Weapons Totals
  weapons_count = get_weapon_count(CONN)
  for k,v in weapons_count.items():
    print(f'{k} : {v}')
  print (f'Total : {sum(weapons_count.values())}')

  # Items per Character
  items_per_char = get_item_count_per_character(CONN) 
  for ipc in items_per_char:
    print(ipc)

  # Weapons per Character
  weapons_per_char = get_weapon_count_per_character(CONN)
  for wpc in weapons_per_char:
   print(wpc)

  #Average Items per Character
  items_avg = get_item_avg(CONN)
  print(f'The average number of items per character is {items_avg:.2f}')

  # Average Weapons per Character
  weapons_avg = get_weapon_avg(CONN)
  print(f'The average number of weaons per character is {weapons_avg:.2f}')

  # Close connection to database
  CONN.close()

if __name__ == "__main__":
  main()



  






