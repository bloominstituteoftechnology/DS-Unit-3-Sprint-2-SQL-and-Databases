
# This the file containing the class mongo_loader which will help 
# to load to the mongo database.  It is used in the assignment 3.

import pymongo
import os
from dotenv import load_dotenv
import sqlite3
from pymongo.errors import BulkWriteError

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
        self.databases = {}
        self.postgres_connection = postgres_connection

        self.sql_tables = {}

        # These are the databases that the 
        #self.databases = {"num_databases":0}

        
            

        
    
    # Method to get all the table names from the sql database
    def get_sql_table_names(self):
        query = """

            SELECT name FROM sqlite_master
            WHERE type='table'
            ORDER BY name;
        """      
        curs = self.sql_connection.cursor()
        curs.execute(query)
        result = curs.fetchall()
        # name is first in a tuple in list
        the_list = []
        for t in result:
            the_list.append(t[0])
         
        return the_list

    # Method to return the client 
    def get_client(self):
        return self.client
    
    # This method will make collection object and will just use a 
    def make_database(self, name):
        db = self.client[name]
        self.databases[name] = db
        #print(db)
        return db 
    #def make_database(self, name):
        

    # This is a method that will return the collection asked for
    def get_database(self, name):
        return self.databases.get(name, "Nope")



    # This is a method that will get the data
    # from an sql and store it in memory
    # If store is set to true then the instance 
    # of this class will store the table in a 
    # dictionary
    def sql_to_list_of_tuples_data(self, table_name, store=True):
        if self.sql_connection == None:
            return "There is no sql connection"
        s_curs = self.sql_connection.cursor()
        self.sql_cursor[table_name] = s_curs
        select_all_quer = "SELECT * FROM  " + table_name
        s_curs.execute(select_all_quer)
        the_table = s_curs.fetchall()
        #checking to see if this will work
        
        #add to the dictionary
        if store == True:
            self.sql_tables[table_name] = the_table
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
        
        return self.sql_tables.get(table_name, "Nope")
        


   
    def sql_to_list_of_tuples_data_multiple_tables(self, table_names_list):
        """ 
        This method will be able to get the multiple
        tables and then store them in a dictionary.
        The tables are passed in as a list of strings
        will return a list with the tables in it

        """
        table_list = []
        for i in range(len(table_names_list)):
            table_list.append(self.sql_to_list_of_tuples_data(table_names_list[i]))
        return table_list    



    def sql_to_list_of_tuples_if_not_exist(self, table_name_or_list_tables):
        """
        This method will store the table data as a list of tuples.
        It will pull it out of the sql and prepare it to be ready to be added to the 
        mongodb.

        It uses internally the sql_to_list_of_tuples_data_multiple_tables
        """
        if isinstance(table_name_or_list_tables, str):
            table_name_or_list_tables = list(table_name_or_list_tables)
        for table in table_name_or_list_tables:
            the_table = self.get_stored_sql_table(table)
            
            if the_table == "Nope":
                self.sql_to_list_of_tuples_data(table)



    # This method will return the column names of the 
    # tables for sql
    
    def get_column_names_sql_table(self, table_name):
        if self.sql_cursor == None:
            print("There is no cursor to use this method or you didn't pass in the table you wanted to use")
        columns = []
        for column  in self.sql_cursor.get(table_name).description:
            columns.append(column[0])
        return columns
    



    def get_collection(self, collection_name, db_name=None):
        """
        This method will retun the collection.  If it is 
        found.  if the db name is not passed in it will return the 
        first found collection with the name specified.  
        This will not guarrantee from which db the collection 
        is comming from.
        """
        if db_name == None:
            for db_name in self.databases:
                ans = self.databases.get(db_name, "Nope")
                if ans != "Nope":
                    break
        else:
            ans = self.databases.get(db_name, "Nope")  

        if ans == "Nope":
            return None
        # Getting the list of the collections in the 
        # database
        collection_list = ans.list_collection_names()
        if collection_name in collection_list:
            coll = ans.get_collection(collection_name)
            return coll
        
  
    
    

    
    def load_data_from_sql_table(self, collection_name, db_name, table_name):
        """
        This method will load the table into the mongodb
        It internally will call the __make_list_of_dict method 
        then use the client to insert_many. Tables will need to 
        be already stored into the class using 
        "sql_to_list_of_tuples_data_multiple_tables()" or "sql_to_list_of_tuples_data()" 
        inorder to use this method.

        """
        table_row_dict_list = self.__make_list_of_dict(table_name)
        
        db = self.databases.get(db_name, "Nope")
        
        if db == "Nope":
            db = self.make_database(db_name)
        # Need to now make the collection that will hold
        # The documents
        collection = db[collection_name]
       
        # using the collection
        collection.insert_many(table_row_dict_list)

        #self.client.


  
                


    def delete(self, query, collection_name=None, many=False, db_name=None, collection=None):
        """
            This method is to delete from collections.
            You can specify if you want to use the delete_many
            or the delete_one call from pymongo by using the 
            many flag which is default False, so it will use
            the delete_one call.  You can pass in the database name 
            if there are two tables on different databases with 
            the same name.  If there is only one then you can leave 
            db_name as None. 
        """
        if collection == None:
            collection = self.get_collection(collection_name=collection_name, db_name=db_name)
        if many == False:
            collection.delete_one(query)
        else:
            collection.delete_many(query)

    



    def load_if_not_exist(self, collection_name, db_name, table_name, max_rows=None):
        """
        THIS METHOD WILL CREATE THE DATABASE AND THE COLLECTION IF THEY DON'T EXIST.

        This method will load the table into the mongo database only if the 
        if the database is not present. If the database is present if the
        collection not made or empty.  Or if you give a row count which the 
        collection must not be over in the number of documents.
        Max rows means the number of rows that if the document has then the 
        program should not load documents to the collection
        """
        build = False
        collection = None

        db = self.get_database(db_name) 
        if db == "Nope":
            # Need to create the database
            db = self.make_database(db_name)
            build = True

        if build == False:
            # Need to check if there is a collection
            collection = self.get_collection(collection_name, db_name=db_name ) 
        

        if collection == None:
            build = True
        else:
            # Will only get in here if there is a collection
            # Need to check the number of rows
            number = collection.count_documents({})
            if max_rows == None:
                max_rows = 1
            if number < max_rows:
                build = True
        # Now loading to the database
        if build == True:
            self.load_data_from_sql_table(collection_name, db_name , table_name)
        
        return         


    def load_sql_to_mongo_many(self, db_name, table_name_list):
        """
        This method will load more than one table to the mongo database in their 
        own collection.  If the the table already is in then, it will not be loaded
        with this method. 
        """
        for table in table_name_list:
            self.load_if_not_exist(collection_name=table, db_name=db_name, table_name=table)

    # Inner method
    def __each_row_as_dict(self, list_tup):
        """
            Inner method that will make each row of the table
            dictionary
        """
        the_dict = {}
        for k, v in list_tup:
            the_dict[k] = v
        return the_dict



    
    # Inner method 
    def __make_list_of_dict(self, table_name):
        """
            This is a method that will turn the table into
            a list of dictionaries.
            Each row will be a new dictionary.
            tables will need to already be processed into list_of_tuples
            before this method can be used.
        """
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
            the_dict = self.__each_row_as_dict(list_of_tuples)
            table_row_dict_list.append(the_dict)
        
        return table_row_dict_list

   

   # This method is an inner method the will get the string 
    # for the connnction to the mongo database.
    def __get_connection_string(self, MONGO_USER, MONGO_PASSWORD, CLUSTER_NAME):
       # "mongodb+srv://user_byu:<password>@cluster0-bj6wb.mongodb.net/test?retryWrites=true&w=majority"
       con_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
       return con_uri