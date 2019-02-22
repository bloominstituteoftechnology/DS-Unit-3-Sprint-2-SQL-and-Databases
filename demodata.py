#!/usr/bin/env python 3

import pandas as pd
import sqlite3

# Make connection object
connection = sqlite3.connect('demo_data.sqlite3')
c = connection.cursor()

# Create table
c.execute('''CREATE TABLE
          ''')

# Output some data
