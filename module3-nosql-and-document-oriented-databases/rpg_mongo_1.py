"""
RPG MongoDB :: Loads RPG test data into a mongo db cluster.
Author :: Tobias Reaper | github.com/tobias-fyi
"""

# %% Imports
import pymongo
import os
import json

from pprint import pprint

# %% Construct path working directory
# Get the full filepath from envirovars
dir_path = os.environ["DIR_323"]

os.chdir(dir_path)  # Change working directory

# Just to be sure that we're in the correct directory
assert os.getcwd() == dir_path

# %% Load json into python object

# Define name of json file
json_file_name = "rpg_data.json"

# Open file and read it into a python object
with open(json_file_name) as f:
    rpg_data = json.load(f)

pprint(rpg_data)

# %% Split up Python object
# The goal here is to reorganize the data such that
# each row is contained within its corresponding model.
# This way, I can use the name of the model as the name
# of the MongoDB document.

# Set to hold distinct data models
rpg_modelset = set()

for row in rpg_data:  # Loop to build set of existing models
    rpg_modelset.add(row["model"].split(".")[1])

# TODO: Use list comprehension to clean up loops

# %% Create dictionaries for each model
# They will be dictionaries inside of rpg_models
rpg_models = {}

# Loop to nest a dict for each model inside rpg_models
for model in rpg_modelset:
    rpg_models[f"{model}"] = {}

# %% Now add all the data into the new data structure
# Loop through rows, this time adding them to their respective nested dict
for row in rpg_data:
    rpg_models[f'{row["model"].split(".")[1]}'][row["pk"]] = row["fields"]

# %% Connect to the cluster
# Password is URL-encoded
client = pymongo.MongoClient()
db = client.rpg_db

# %% Count documents
db.rpg_db.count_documents({"x": 1})

# %%
