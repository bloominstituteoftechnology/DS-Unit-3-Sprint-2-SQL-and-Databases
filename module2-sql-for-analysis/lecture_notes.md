What is postgress?
- elephantSQL is a hosted postgress database.
- people use sqllite for staging hosting, but postgress sql is for scaling up.

RDMS: Relational Database Management System
- mySQL - most used SQL Database
- postgress - second most. Used most for mid-large companies.

elephantSQL: Called this because elephants never forget.
- Does not lose much when you scale up.
- unlimited amount of databases.

starting:
- create an instance
- tools on left
  - details:
    - Server - it's a host, a subdomain of elephantSQL
    - Browser - we can do SQL queries.
      - ``/* comment */``
      - ``opening a table``
      - ``\dt`` command for opening tables.

When not to use serial numbers?
- security issue.

Create table
- CREATE TABLE test_table (id SERIAL PRIMARY KEY, name varchar(40) NOT NULL, data JSONB);    
  - made table
- INSERT INTO test_table (name, data) VALUES
('a row name', null), ('a second row',
'{"a": 1, "b": ["dog", "cat", 42], "c": true}'::JSONB
);
  - making rows
- DELETE FROM test_table
WHERE name = 'a row name'
  - delete rows

In the same way that yesterday we used sqlite3 to connect to the sqlite database, and today we're using psychopg to connect to postgress
- we are going to open up a connection to postgress to elephant sql and also to the sql database, in order to have a data pipeline where we clone information from the sql database and can put it in the elephantSQL.

[Switching to lecture_notes.py]
