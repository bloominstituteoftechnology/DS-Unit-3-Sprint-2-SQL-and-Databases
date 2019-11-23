import sqlite3

connect = sqlite3.connect('demo_data.sqlite3')
cursor = connect.cursor()

query = '''
CREATE TABLE demo (
    s NCHAR(1),
    x INT,
    y INT
);
INSERT INTO demo
VALUES 
('g', 3, 9),
('v', 5, 7),
('f', 8, 7)
;
'''
cursor.executescript(query)
cursor.commit()

query = '''SELECT COUNT(*) FROM demo'''
cursor.execute(query).fetchall()

query = '''
SELECT COUNT(*) FROM demo
WHERE x >= 5 AND y >= 5
;
'''
cursor.execute(query).fetchall()

query = '''
SELECT COUNT(DISTINCT y)
FROM demo
;
'''
cursor.execute(query).fetchall()