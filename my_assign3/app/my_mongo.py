
# This is the file that will run the script to load the
# rpg file into the mongo database. 
# It will utilize the class mong_loader

from my_assign3.app.mongo_loader import Mongo_loader
import os

m = Mongo_loader()

m.make_database("rpg")

# Will be getting the path for the sql connection
rpg_path = os.path.join(os.path.dirname(__file__), "..", 
                                        "data","rpg_db.sqlite3")

m.make_sql_connection(rpg_path)

m.sql_to_list_of_tuples_data("charactercreator_character")
m.sql_to_list_of_tuples_data("armory_item")

m.get_column_names_sql_table("charactercreator_character")
cols = m.get_column_names_sql_table("armory_item")

m.load_data_from_sql_table("charactercreator_character", "rpg", "charactercreator_character")

char_creator = m.get_collection("charactercreator_character")

print(char_creator.count_documents({})) # Trying to find the
