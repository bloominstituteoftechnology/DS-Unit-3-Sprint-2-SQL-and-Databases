import pandas as pd
import sqlite3
import psycopg2


dbname = ''        # Insert your own database name here
user = ''          # Your own username
password = ''      # Your own password
host = ''          # You own server


def df_create(file_name):
    '''Create cleaned dataframe from specified file'''
    df = pd.read_csv(file_name)

    # Replace apostrophes in name column to avoid SQL confusion
    df['Name'] = df['Name'].str.replace("'", '', regex=True)

    # Replace / and spaces in column names with underscores
    df.columns = df.columns.str.replace('/', "_")
    df.columns = df.columns.str.replace(' ', '_')

    return df

df = df_create('titanic.csv')

# Instantiate connection to sqlite3
# Convert df to SQL
t_conn = sqlite3.connect('titanic.sqlite3')
df.to_sql('titanic', t_conn, index=False)

# Instantiate sqlite3 cursor
t_curs = t_conn.cursor()

# save SQL tabular data to people variable
people = t_curs.execute('SELECT * FROM titanic').fetchall()

# Instantiate postgresql connection & cursor
tpg_conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)
tpg_curs = tpg_conn.cursor()

# Create postgresql table
create_titanic_table = '''
    CREATE TABLE titanic (
        Survived INT,
        Pclass INT,
        Name VARCHAR(500),
        Sex VARCHAR(7),
        Age INT,
        Siblings_Spouses_Abroad INT,
        Parents_children_Abroad INT,
        Fare REAL
        )
    '''

tpg_curs.execute(create_titanic_table)

# Add sqlite3 data to postgresql table
for person in people:
    insert_person = """
        INSERT INTO titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Abroad, Parents_Children_Abroad, Fare)
        VALUES """ + str(person[:]) + ';'
    # print(insert_character)
    tpg_curs.execute(insert_person)

# Close cursor, commit connection to ElephantSQL
tpg_curs.close()
tpg_conn.commit()
