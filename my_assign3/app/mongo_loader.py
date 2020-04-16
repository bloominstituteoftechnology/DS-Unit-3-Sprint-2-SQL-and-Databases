
# This the file containing the class mongo_loader which will help 
# to load to the mongo database.  It is used in the assignment 3.

import pymongo
import os
from dotenv import load_dotenv
import sqlite3

#client = pymongo.MongoClient("mongodb+srv://user_byu:<password>@cluster0-bj6wb.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test



class Mongo_loader:


    
    #Each instance of the the Mongo_loader will make a new
    # connection if one is not given
    def __init__(self, client=None, MONGO_USER=None, MONGO_PASSWORD=None, CLUSTER_NAME=None,
                    sql_connection=None, postgres_connection=None):
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
        self.sql_connection = sql_connection
        self.sql_cursor = {}
        self.collections = {}
        self.postgres_connection = postgres_connection

        self.sql_tables = {}

        # These are the databases that the 
        self.databases = {"num_databases":0}

        
            

        
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
    def make_collection_database(self, name):
        collection_db = self.client[name]
        self.collections[name] = collection_db
        return collection_db 
    #def make_database(self, name):
        

    # This is a method that will return the collection asked for
    def get_collection(name):
        return self.collections.get(name, "Nope")
        
    # This is a method that will get the data
    # from an sql and store it in memory
    # If store is set to true then the instance 
    # of this class will store the table in a 
    # dictionary
    def get_sql_data(self, table, store=True):
        if self.sql_connection == None:
            return "There is no sql connection"
        s_curs = self.sql_connection.cursor()
        self.sql_cursor[table] = s_curs
        select_all_quer = "SELECT * FROM  " + table
        s_curs.execute(select_all_quer)
        the_table = s_curs.fetchall()
        #checking to see if this will work
        #print(f"This the table type of {table} {type(the_table)}")
        #print(f"This is the length {len(the_table)}")
        #add to the dictionary
        if store == True:
            self.sql_tables[table] = the_table
        return the_table

    # This is a method that will make the connection for the
    # sql on sqlite3    
    def make_sql_connection(self, sql_path):      
        connection = sqlite3.connect(sql_path)
        self.sql_connection = connection
        return connection

    # This method will get the sql tables that are stored in the 
    # dictionary for the
    def get_stored_sql_table(self, table_name):
        
        return self.sql_tables.get(table_name, "Table not found")
        


    # This method will be able to get the multiple
    # tables and then store them in a dictionary.
    # The tables are passed in as a list of strings
    # will return a list with the tables in it
    def get_sql_data_multiple_tables(self, table_names_list):
        table_list = []
        for i in range(len(table_names_list)):
            table_list.append(self.get_sql_data(table_names_list[i]))
        return table_list    

    # This method will return the column names of the 
    # tables for sql
    
    def get_column_names_sql_table(self, table_name):
        if self.sql_cursor == None:
            print("There is no cursor to use this method or you didn't pass in the table you wanted to use")
        columns = []
        for column  in self.sql_cursor.get(table_name).description:
            columns.append(column[0])
        return columns
    
    # This is a method that will turn the table int
    # a list of dictionaries.
    # Each row will be a new dictionary

    def __make_table_list(self, table_name):
        table_row_dict_list = []
        table_columms  =  self.get_column_names_sql_table(table_name)
        table_tuple_list =self.get_stored_sql_table(table_name)

        if table_tuple_list == "Table not found":
            print("This table is not found")
            return
            
        for the_tuple in table_tuple_list:
            list_of_tuples = []
            for i in range(len(the_tuple)):
                list_of_tuples.append((table_columms[i], the_tuple[i]))
            the_dict = self.__make_list_tuples(list_of_tuples)
            table_row_dict_list.append(the_dict)
        
        return table_row_dict_list

    

    # This method will load the table into the mongodb
    # It internally will call the __make_table_list method then use the
    # client to insert_many
    def load_data_from_sql_table(self, table_name):
        table_row_dict_list = self.__make_table_list(table_name)

        the_collection = self.collections.get(table_name, "Nope")
        
        if the_collection == "Nope":
            the_collection = self.make_collection_database(table_name)
        
        # using the collection
        the_collection.insert_many()

        self.client.



    def __make_list_tuples(self, list_tup):
        the_dict = {}
        for k, v in list_tup:
            the_dict[k] = v
        return the_dict

                
        


    # them in a 
    # This method will make a connection and then return 
    # it when called.
    #def makeConnection(self):


   