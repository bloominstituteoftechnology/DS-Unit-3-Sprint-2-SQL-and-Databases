query=
"""
CREATE TABLE LendingClub (
    "id" INT,
    "member_id" NUMERIC(8, 1),
    "loan_amnt" NUMERIC(6, 1),
    "funded_amnt" NUMERIC(6, 1),
    "term" TEXT,
    "int_rate" TEXT,
    "grade" TEXT,
    "home_ownership" TEXT,
    "loan_status" TEXT
);
"""


with open('LendingClub_trunc.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute("INSERT INTO LendingClub VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        row)



query = """'INSERT INTO LendingClub VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s),row"""


743268,941494.0,15000.0,15000.0, 36 months, 13.49%,C,RENT,Fully Paid


import csv
import psycopg2 as pg

conn = pg.connect("host=localhost dbname=dataquest user=sammylee")
cur = conn.cursor()

