# Sprint 2 Module 2 Assignment

Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a PostgreSQL database. We walked through most of these
steps in lesson but see if you can finish moving the `charactercreator_character` table.

Next, set up a new table for the Titanic data (`titanic.csv`) - spend some time
thinking about the schema to make sure it is appropriate for the columns.
[Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
be useful. Once it is set up, write a `insert_titanic.py` script that uses
`psycopg2` to connect to and upload the data from the csv. Then add the file to
your repo. Fianlly, start writing PostgreSQL queries to explore the data!

Please upload the `insert_titanic.py` python file to Canvas.
