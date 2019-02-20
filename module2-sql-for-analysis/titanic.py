import psycopg2 as pgres
import pandas as pd

ele_conn = ''
ele_cur=None


# ___ Connect to ElephantSQL db _________
def conx_elephant(conx_str):
    # instantiate and return connection obj
    cnx = pgres.connect(conx_str)
    return cnx


# _____ DROP table ____________
def drop_table(tbl_name):
    qry = "DROP TABLE " + tbl_name
    ele_cur.execute(qry)
    ele_conn.commit()
    return


# ---- CREATE a new table------------------
def create_table(tbl_name, fields_str):
    qry = "CREATE TABLE " + tbl_name + 
    ele_cur.execute(qry)
    ele_conn.commit()
    return


# ___________ INSERT data ___________________________
def insert_data():
    cur = ele_conn.cursor()
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
    return

# _______  SELECT data _______________________________
# rows = cur.execute("SELECT * FROM test_table;")
# for row in rows:
#    print(row)
# cur.fetchone()
# cur.fetchall()


def run_conversion(ele_cur):
    return


def main():
    # ____ Connect to an ElephantSQL __________
    conx_str = """
    dbname='zoafqkfp' user='zoafqkfp'
    host='stampy.db.elephantsql.com'
    password='MCJu21HwCynkStIs3FOmV-xHXSAXOSDD'
    """
    ele_conn = conx_elephant(conx_str)
    
    # ____ create cursor ___
    ele_cur = ele_conn.cursor()  
    
    # ____ Port titanic.csv to Postgres ___
    # run_conversion(ele_cur)

    # ___ end main ___________
    ele_cur.close()   # close cursor
    ele_conn.close()  # close connection   
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
