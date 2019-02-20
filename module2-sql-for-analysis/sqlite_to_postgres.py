import psycopg2

# Connect to an existing database
conx_str = """
dbname='zoafqkfp' user='zoafqkfp'
host='stampy.db.elephantsql.com'
password='MCJu21HwCynkStIs3FOmV-xHXSAXOSDD'
"""
conx = psycopg2.connect(conx_str)
cur = conx.cursor()



# ---- CREATE a new table------------------
qry = "CREATE TABLE test_table (id serial PRIMARY KEY, name varchar(40) NOT NULL, data JSONB);"
cur.execute(qry)
conx.commit()

# ---- INSERT data
# fill aquery placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur = conx.cursor()
new_data = [("Gretsch", {'year': '1975', 'color': 'silver'}),
            ("Fender", {'year': '1972', 'color': 'blonde'}),
            ("Rickenbacker", {'year': '1965', 'color': 'red'}),
            ("Gibson", {'year': '1959', 'color': 'sunburst'}),
            ("Taylor", {'year': '1992', 'color': 'spruce'})]
in_qry = "INSERT INTO test_table (name, data) VALUES (%s, (%s+'::JSONB');"
print(in_qry)
# for name, data in new_data:
#     cur.execute(in_qry, (name, data))
# conx.commit()

# ---print contents of table
# rows = cur.execute("SELECT * FROM test_table;")
# for row in rows:
#    print(row)
# cur.fetchone()
# cur.fetchall()

# ------DROP  table -----------
qry = "DROP TABLE test_table"
cur.execute(qry)
conx.commit()

# --- we're done here ------
cur.close()
conx.close()
