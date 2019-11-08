"""
Titanic Postgres :: Loads titanic.csv into local Postgres instance.
"""

# %% Imports
import os
from pprint import pprint
import psycopg2
import pandas as pd

import janitor

# %% Move to working directory
cwd = os.environ["DIR_324"]
os.chdir(cwd)
print(os.getcwd())

# %% Local imports
# I will be putting all of my queries and functions in a package 'tiq'
import tiq

# %% Queries

# Standard select statement
select = """
    SELECT
        *
    FROM
        passengers;"""

# %%
