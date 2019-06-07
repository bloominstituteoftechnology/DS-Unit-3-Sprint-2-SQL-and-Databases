# In the Northwind database, what is the type of relationship between the Employee and Territory tables?
**The relationship is one-to-many, mediated through the EmployeeTerritory table. Each employee is connected to several different territories, each of which may have only one employee operating in it.**
# What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

  **Document stores are appropriate where a rigid schema structure is not appropriate; for example, we might use a document store if we're operating a database for an online store, where different types of items have different characteristics, subject to change at the company's whim. We might, for example, wish to include a field measuring an item's softness for bedding, but such a field wouldn't be appropriate for a description of a bedframe. Schemaless databases allow for this kind of on-the-fly modification of properties.**

  **For that reason, we would prefer to use a traditonal relational database in circumstances where we know in advance what kind of data is going to be relevant and would like to enforce a pre-determined structure on data, and particularly when we want to be able to make consistent queries that are predictable and easy to make--since we already know the schema structure in advance. So if we know we're going to make lots of queries, for example if we would like to perform automated data analysis on sales by region or some other characteristic, we would probably prefer a relational database to a document store.**

# What is "NewSQL", and what is it trying to achieve?
**NewSQL is in some sense a bridge between the traditional relational style of SQL and the more flexible schema-free style of NoSQL. It's designed to retain the scalability of NoSQL while still guaranteeing the ACID reliability properties of SQL.**
