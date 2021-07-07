import sqlite3

conn = sqlite3.connect('')
curs = conn.cursor()


curs.execute(
"""
CREATE TABLE demo (
s str,
x int,
y int
);
"""
)

conn.commit()

curs.execute(
"""
INSERT INTO demo (
 s,
 x,
 y,)
VALUES
 (
 'g',
 'v',
 'f'),
 (
 3,
 5,
 8),
 (
 9,
 7,
 7);
)
"""
)

conn.commit()

# Count how many rows you have - it should be 3!
curs.execute(
"""
SELECT
    count(*)
FROM
    demo;
"""
)

# How many rows are there where both x and y are at least 5?
curs.execute(
"""
SELECT
    x,
    y,
    count(*)
FROM
    demo
WHERE
    x >= 5
AND y >= 5;
"""
)

# How many unique values of y are there?
curs.execute(
"""
SELECT
    COUNT(DISTINCT y)
FROM
    demo;
"""
)
