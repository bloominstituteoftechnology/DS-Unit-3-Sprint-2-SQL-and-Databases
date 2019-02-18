from load_query import *

data = Load_Data('rpg_db.sqlite3')
character_count = data.make_query('COUNT(DISTINCT(name))', 'charactercreator_character')
print(f'The number of characters is {character_count[0]}')

character1 = data.make_query('*', 'charactercreator_character', 'LIMIT', '5')
print(f'The number of characters is {character1}')