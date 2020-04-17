
# This is the file that will run the script to load the
# rpg file into the mongo database. 
# It will utilize the class mong_loader

from my_assign3.app.mongo_loader import Mongo_loader
import os

m = Mongo_loader()


# Will be getting the path for the sql connection
rpg_path = os.path.join(os.path.dirname(__file__), "..", 
                                        "data","rpg_db.sqlite3")

m.make_sql_connection(rpg_path)

rpg_list = ["armory_item", "armory_weapon", "charactercreator_character", "charactercreator_character_inventory",
            "charactercreator_cleric", "charactercreator_fighter", "charactercreator_mage",
            "charactercreator_necromancer", "charactercreator_thief" ]

m.sql_to_list_of_tuples_if_not_exist(rpg_list)



# This will not load again if already loaded
m.load_sql_to_mongo_many('rpg', rpg_list)





# Telling the number of characters in the collection charactercreator_character
char_creator = m.get_collection("charactercreator_character")
print(char_creator.count_documents({})) # Trying to find the number or rows
