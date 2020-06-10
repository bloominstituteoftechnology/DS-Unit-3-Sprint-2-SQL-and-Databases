import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('titanic.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s ,%s, %s)",
        row
    )
conn.commit()