def run_queries(cur):
    # _________ HOW MANY ROWS IN DEMO ______________
    qry = 'SELECT COUNT(*) FROM demo ORDER BY demo.x;'
    for row in cur.execute(qry):
        print('demo table has ', row[0], ' rows')

    # _________ HOW MANY ROWS IN DEMO ______________
    qry = '''
    SELECT COUNT(*)
    FROM demo
    WHERE demo.x >= 5 AND demo.y >= 5
    ORDER BY demo.x;
    '''
    for row in cur.execute(qry):
        print('There are ', row[0], ' rows where noth x and y are at least 5')
    return
