import os
import pandas as pd
import pymongo
from dotenv import load_dotenv

USER = os.getenv["MONGO_USER", default="OOPS"]
PASS = os.getenv["MONGO_PASS", default="OOPS"]

client = pymongo.MongoClient("mongodb+srv://{USER}:{PASS}@dpst5-ryandavidson-dyw1j.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

client.titanic.titanic.drop()

titanic_df = pd.read_csv("titanic.csv")
docs = [
    {
        "titanic_id": titanic_id,
        "Survived": survived,
        "Pclass": pclass,
        "Name": name,
        "Sex": sex,
        "Age": age,
        "siblings_or_spouses_aboard": siblings_or_spouses_aboard,
        "parents_or_children_aboard": parents_or_children_aboard,
        "Fare": fare
    } for titanic_id, survived, pclass, name, sex, age, siblings_or_spouses_aboard, parents_or_children_aboard, fare
    in titanic_df.itertuples()
]

client.titanic.titanic.insert_many(docs)