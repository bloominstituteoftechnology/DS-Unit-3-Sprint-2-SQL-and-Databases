import psycopg2


dbname = 'tjqpupzb'
user = 'tjqpupzb'
password = 'qFi0L1iCGKRHqfOaMcQlHy1806Y7dNKc'
host = 'rajje.db.elephantsql.com' 

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

query_list = [
'''SELECT survived, COUNT(*)
FROM titanic
GROUP BY survived;
''',
'''SELECT pclass, COUNT(*)
FROM titanic
GROUP BY pclass
ORDER BY pclass ASC;
''',
'''SELECT pclass, survived, COUNT(Survived)
FROM titanic
GROUP BY pclass, survived
ORDER BY pclass, survived;
''',
'''SELECT survived, SUM(age)/COUNT(survived)
FROM titanic
GROUP BY survived;
''',
'''SELECT pclass, SUM(age)/COUNT(pclass)
FROM titanic
GROUP BY pclass
ORDER BY pclass ASC;
''',
'''SELECT pclass, AVG(fare)
FROM titanic
GROUP BY pclass
ORDER BY pclass ASC;
''',
'''SELECT survived, AVG(fare)
FROM titanic
GROUP BY survived;
''',
'''SELECT pclass, CAST(AVG(siblings_or_spouses_aboard) AS FLOAT)
FROM titanic
GROUP BY pclass
ORDER BY pclass ASC;
''',
'''SELECT survived, CAST(AVG(siblings_or_spouses_aboard) AS FLOAT)
FROM titanic
GROUP BY survived;
''',
'''SELECT pclass, CAST(AVG(parents_or_children_aboard) AS FLOAT)
FROM titanic
GROUP BY pclass
ORDER BY pclass ASC;
''',
'''SELECT survived, CAST(AVG(parents_or_children_aboard) AS FLOAT)
FROM titanic
GROUP BY survived;
''',
'''SELECT name
    FROM titanic
    GROUP BY name
    HAVING COUNT(*)>1;
''']

question_list = [
    'How many passengers survived, and how many died?',
    'How many passengers were in each class?',
    'How many passengers survived/died within each class?',
    'What was the average age of survivors vs nonsurvivors?',
    'What was the average age of each passenger class?',
    'What was the average fare by passenger class?',
    'What was the average fare by survival?',
    'How many siblings/spouses aboard on average, by passenger class?',
    'How many siblings/spouses aboard on average, by survival?',
    'How many parents/children aboard on average, by passenger class?',
    'How many parents/children aboard on average, by survival?',
    'Do any passengers have the same name?'
    ]

sp_dict = {'0': 'Perished', '1': 'Survived'}
class_dict = {'1':'1st class', '2':'2nd class', '3': '3rd class'}
for x, question in enumerate(question_list):
    s1 = False
    c1 = False
    s2 = False
    print(question)
    query = query_list[x]
    curs.execute(query)

    # change values from queries based on the query, then print each row
    q_split = query.split(" ")
    if q_split[1] == 'survived,':
        s1 = True
    elif q_split[1] == 'pclass,':
        c1 = True
    else:
        print('No')
    if q_split[2] == 'survived,':
        s2 = True
    rows = curs.fetchall()

    for row in rows:
        row = (str(row)[1:].split(', '))
        if s1:
            row[0] = sp_dict.get(row[0])
        elif c1:
            row[0] = class_dict.get(row[0])
        if s2:
           row[1] = sp_dict.get(row[1])
        print(row)