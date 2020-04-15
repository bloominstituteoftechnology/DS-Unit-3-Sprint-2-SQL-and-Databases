
# This the file containing the class mongo_loader which will help 
# to load to the mongo database.  It is used in the assignment 3.

import pymongo
import os
from dotenv import load_dotenv

#client = pymongo.MongoClient("mongodb+srv://user_byu:<password>@cluster0-bj6wb.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test



class Mongo_loader:


    
    #Each instance of the the Mongo_loader will make a new
    # connection if one is not given
    def __init__(self, client=None, MONGO_USER=None, MONGO_PASSWORD=None, CLUSTER_NAME=None):
        # Load_dotenv will make it so that 
        # the variables in the .env file are loaded
        # as environment variables.   
        if client == None:
            if MONGO_PASSWORD == None or MONGO_USER == None or CLUSTER_NAME ==None:
                load_dotenv()
                MONGO_USER = os.getenv("MONGO_USER")
                MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
                CLUSTER_NAME = os.getenv("CLUSTER_NAME")

            """ # Storing the mongo required credential inorder to connect
            self.MONGO_PASSWORD = MONGO_PASSWORD
            self.MONGO_USER = MONGO_USER
            self.CLUSTER_NAME = CLUSTER_NAME """

            # Getting the string that will help to connect to the 
            # Mongo database.
            con_uri = self.__get_connection_string(MONGO_USER=MONGO_USER, MONGO_PASSWORD=MONGO_PASSWORD,
                                                        CLUSTER_NAME=CLUSTER_NAME)

            client = pymongo.MongoClient(con_uri)
        
        # Storing the client in this instance
        self.client = client
        # These are the databases that the 
        self.databases = {"num_databases":0}

         # checking the connection
        #print("The client", type(client)) 
            

        
    # This method is an inner method the will get the string 
    # for the connnction to the mongo database.
    def __get_connection_string(self, MONGO_USER, MONGO_PASSWORD, CLUSTER_NAME):
       # "mongodb+srv://user_byu:<password>@cluster0-bj6wb.mongodb.net/test?retryWrites=true&w=majority"
       con_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
       return con_uri
           

    # Method to return the client 
    def get_client(self):
        return self.client
    
    # This method will make the database and will just use a 
    def make_database(self, name):
        db = self.client[name]
        print(type(db), db)
        return db 
    #def make_database(self, name):
        
        
# If a connection is sent in then the mongo_loader will 
        # use it.
        
        
          
        
    # This method will make a connection and then return 
    # it when called.
    #def makeConnection(self):


   