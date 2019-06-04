import sqlite3 

# open a connection to sqlite database

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

## test queries

# count number of rows
query0 = ('SELECT COUNT(*) FROM review;')
request0 = curs.execute(query0)

print('# of rows: {}'.format(request0.fetchone()[0]))

# How many users who reviewed at least 100 Nature in 
# the category also reviewed at least 100 in the Shopping category?

query1 = ('''
    SELECT COUNT(*) 
    FROM review AS r 
    WHERE r.Nature >= 100 AND r.Shopping >= 100
    ''')

request1 = curs.execute(query1)

print('# users reviewed at least 100 in Nature and Shopping: {}'.format(
    request1.fetchone()[0]))

# What are the average number of review for each category?
categories = ['Sports', 'Religious', 'Nature', 'Theatre', 
            'Shopping', 'Picnic']

for _ in categories:
    query = ('''
        SELECT AVG(r.{})
        FROM review AS r
        '''.format(_))
    request = curs.execute(query)

    print('AVG # of reviews for {}: {}'.format(
        _, request.fetchone()[0]))