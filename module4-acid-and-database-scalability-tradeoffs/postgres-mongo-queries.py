
import pymongo
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    mongo_queries()

    postgres_queries()

def mongo_queries():
    #connect to mongo db
    USER = os.getenv('MONGO_USER', default = 'oops')
    PASSWORD = os.getenv('MONGO_PASSWORD', default = 'oops')
    CLUSTER = os.getenv('MONGO_CLUSTER', default = 'oops')

    uri = f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.mongodb.net/test?retryWrites=true&w=majority'

    # How many total Characters are there?
    # TODO

    # How many of each subclass?
    # TODO

    # How many total items?
    # TODO

    # How many items are weapons? 
    # TODO

    # How many are not?
    # TODO

    # How many items does each character have? (first 20)
    # TODO

    # How many weapons does each character have? (first 20)
    # TODO

    # Average, how many items does each character have?
    # TODO

    # Average, how many Weapons does each character have?
    # TODO

def postgres_queries():
    #Connect to postgres
    #TODO
    pass

    # How many passengers survived, and how many died?
    #TODO

    # How many passengers were in each class?
    # TODO

    # How many passengers survived/died within each class?
    # TODO

    # What was the average age of survivors vs nonsurvivors?
    # TODO

    # WHat was the average age of each passenger class?
    # TODO

    #What was the average fare by passenger class? By survival?
    # TODO

    # How many siblings/spouses aboard on average, by passenger class? by Survival?
    # TODO

    # How many paretns/children aboard on average, by passenger class? by survival?
    # TODO

    # Do any passengers have the same name?
    # TODO




if __name__ == "__main__":
    main()