"""first few minutes of this video is mongodb vs postgreSQL"""
- SQLite is really good for prototyping but can't really scale things up. So we'll switch it to sqlite when launching an app or something. SQLite is just a flat file. Is not actually a database

When might you prefer mongodb over postgres?
- postgres - the postgres tool wwe used was called elephantSQL and we connected to it using a package called psychopg. Everything with elephantSQL and psychopg was postgres.
- mongodb is preferable when we have unstructured data. Like news articles. Articles don't fit easily into columns. Companies use mongodb for scaling becuase you don't need a specific schema. So it can be better for early in a project. So sometimes people go from mongodb as prototype to postress. Mongodb: unstructured and best for big data.
- easier to lose data in mongodb than postgres. That's a consequence of doing big data work.
- Mongodb is non relational and nonstructured. It is nosql, so it isn't built on standard sql or relational algebra.

Think about the relational algebra lesson. What were some of the relationships and give a real world ex
- Relational algebra 3 relationships: one to one; one to many; many to many. This relates to SQL in terms of joining SQL tables. Connecting two tables, as we did this week, is a because of joining one to one.
- auxiliary joins are when we have to use an intermediary table. This is a many to many join.

Scaling horizontally vs scaling vertically.
- vertically is about scaling across computers and horizontally is within a machine

newsql - Relational databases that gets best of both worlds. Scales up with big data but keeps maneuverability of SQL. Keeps acid guarantees of relational database systems.

- A - Atomicity: each transaction between user and database is a unique atom unit of work. If one operation fails the data stays the same. Each operation either fails completely or succeeds completely.
- C - Consistency: the databases that make transactions from one database to another must be done from databases in a valid state.
- I - Isolation: Transactions are often entered concurrently. Isolation ensures that all data written to the database is confined to the rules of the database, leaving the databases in the same state that they were in prior to the transactions, as if each transaction was done sequentially.
- D - Durability: once a transaction has been committed it will remain committed even in the case of a system failure.

- ACID guarantees are more common in relational databases then non relational. which means postgres would be more safe than mongodb because it has these acid guarantees.

Cascades and triggers:
- a way to make sure you don't have weird data that relates to something you deleted in your database. They wipe out everything related to the deleted item across all tables.

CAP theorem:
- When talking about distributed data store, it's impossible to provide more than 2 of the following guarantees:
  - Consistency: Every read receives the most recent write or an error
  - availability: Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
  - Partition tolerance: system continues to operate despite an arbitrary number of messages being dropper (or delayed) by the network between nodes.
