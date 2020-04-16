
# This is the file that will run the script to load the
# rpg file into the mongo database. 
# It will utilize the class mong_loader

from my_assign3.app.mongo_loader import Mongo_loader
import os

m = Mongo_loader()

#m.make_database("cat")

# Will be getting the path for the sql connection
rpg_path = os.path.join(os.path.dirname(__file__), "..", 
                                        "data","rpg_db.sqlite3")

m.make_sql_connection(rpg_path)

m.get_sql_data("charactercreator_character")
m.get_sql_data("armory_item")

m.get_column_names_sql_table("charactercreator_character")
cols = m.get_column_names_sql_table("armory_item")

print(cols)