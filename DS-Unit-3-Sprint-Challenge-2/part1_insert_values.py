#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('part1_db.sqlite3')

insert = (
    "INSERT INTO part1 VALUES "
    "('g', 3, 9), "
    "('v', 5, 7), "
    "('f', 8, 7)"
)

curs = conn.cursor()
curs

result = curs.execute(insert)
result

conn.commit()