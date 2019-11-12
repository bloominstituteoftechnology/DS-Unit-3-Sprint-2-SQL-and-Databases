#In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?#
- This is a one to many relationship, from the perspective of EmployeeTerritory. The first reason I knew this was becuase of the .png file that shows us the relationships. To confirm that my reading of the image was right, I looked at the data and there was only one entry for TerritoryId in EmployeeTerritory but many duplicates in Employee. This means that in matching the two tables up, each entry in EmployeeTerritory would be matched to many entries in Employee

#What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
- A situation where a document store is appropriate is when the data does not fit easily into rows and columns, but is better stored in seperate "documents" that can have unique schemas to fit whatever data is stored within them. An example of a time when document store might be used would be for a newspaper. All of the articles would fit within their own documents, or maybe documents of related articles/article types.
- A situation where a document store would not be appropriate is when the information is fairly uniform (has a schema) and can be grouped in relations. This would mean that, while the different tables are related, we could created a neat table of data grouped into different tables that could react with one another based on their relations. An example of a time when we would do this instead of using a document store might be for banking information. Every customer gives the bank similar information (credit score, name, address, etc.), but there might be advantages to making different tables based on kinds of bank accounts or the kind of member they are.


#What is "NewSQL", and what is it trying to achieve?
- NewSQL is a relational database that gets the best of both worlds: it scales up with big data but keeps the maneuverability of SQL. Keeps acid guarantees of relational database systems.

- A - Atomicity: each transaction between user and database is a unique atom unit of work. If one operation fails the data stays the same. Each operation either fails completely or succeeds completely.
- C - Consistency: the databases that make transactions from one database to another must be done from databases in a valid state.
- I - Isolation: Transactions are often entered concurrently. Isolation ensures that all data written to the database is confined to the rules of the database, leaving the databases in the same state that they were in prior to the transactions, as if each transaction was done sequentially.
- D - Durability: once a transaction has been committed it will remain committed even in the case of a system failure.

- ACID guarantees provides safety, and for a long time were common in relational databases but not in document stores (maybe that's no longer true), which tended to make relational databases safer than document stores.
