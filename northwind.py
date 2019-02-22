#!/usr/bin/env python 3

import pandas as pd
import sqlite3

connection = sqlite3.connect('northwind_small.sqlite3')

q_one = pd.read_sql_query("SELECT ProductName, UnitPrice from Product ORDER BY UnitPrice DESC LIMIT 10;", connection)
print('Ten most expensive items from Product are', q_one)

q_two= pd.read_sql_query("SELECT * from Employee;", connection)
print('The average age of an employee at the time of their hiring is', q_two)


# Stretch
# q_three_table = pd.read_sql_query("SELECT * from <table>;", connection)

