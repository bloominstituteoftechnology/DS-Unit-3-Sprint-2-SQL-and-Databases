import pandas as pd
import numpy as np

def load_titanic():
    df = pd.read_csv('titanic.csv')
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("/", "_")
    df['Name'] = df['Name'].str.replace("'", " ")
    
    return df
