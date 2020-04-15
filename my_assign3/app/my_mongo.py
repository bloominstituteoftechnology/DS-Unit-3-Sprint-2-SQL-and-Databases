
# This is the file that will run the script to load the
# rpg file into the mongo database. 
# It will utilize the class mong_loader

from my_assign3.app.mongo_loader import Mongo_loader

m = Mongo_loader()

m.make_database("cat")