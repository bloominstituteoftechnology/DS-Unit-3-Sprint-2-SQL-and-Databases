import sys
import pandas as pd
import psycopg2 as pg

def csv_to_list_of_tuples(filename, **kwargs):
    df = pd.read_csv(filename, **kwargs)
    list_of_tuples = df.apply(lambda x: "({},{},{},{},{},{},{},{})".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]),
                              axis = 1)
    return list_of_tuples

# create_enum_sex = """
#     IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'sex') THEN
#         CREATE TYPE sex AS ENUM
#         (
#             'male', 'female'
#         );
#     END IF;
# """

create_enum_sex = """
        CREATE TYPE sex AS ENUM
        (
            'male', 'female'
        );
"""

sql_create_titanic_table = """CREATE TABLE titanic (
  passenger_id SERIAL PRIMARY KEY,
  survived int,
  pclass int,
  name varchar(50),
  sex varchar(10),
  age real,
  num_siblings_spouses_aboard int,
  num_parents_children_aboard int,
  fare real
);"""

def create_titanic_table(curs):
   # curs.execute(create_enum_sex)
   # conn.commit()
   curs.execute("""DROP TABLE titanic""")
   conn.commit()
   curs.execute(sql_create_titanic_table)
   conn.commit()
   res = csv_to_list_of_tuples('./titanic.csv', header=0, index_col=False)
   print(res[0])
   print("----------- Starting table insert -------")
   curs.execute("INSERT INTO titanic(survived,pclass,name,sex,age,num_siblings_spouses_aboard,num_parents_children_aboard,fare) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (10,11,'a name','male',22.2,2,2,22.7))
   # curs.executemany("INSERT INTO titanic(survived,pclass,name,sex,age,num_siblings_spouses_aboard,num_parents_children_aboard,fare) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", res)
   print("----------- Ended table insert ----------")

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: titanic.py dbname user pwd host")
        sys.exit()
        
    dbname = sys.argv[1]
    user   = sys.argv[2]
    pwd    = sys.argv[3]
    host   = sys.argv[4]

    with pg.connect(dbname=dbname, user=user, password=pwd, host=host) as conn:
        with conn.cursor() as curs:
            create_titanic_table(curs)
