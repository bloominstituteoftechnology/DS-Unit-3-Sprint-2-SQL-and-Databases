#!/bin/bash

#sqlite3 -header -csv ../module1-introduction-to-sql/rpg_db.sqlite3 'select * from charactercreator_character;' > out1.csv

/home/tt/anaconda3/bin/sqlite3 ../module1-introduction-to-sql/rpg_db.sqlite3 <<!
.headers on
.mode csv
.separator '|'
.output out.csv
select * from charactercreator_character;
!
