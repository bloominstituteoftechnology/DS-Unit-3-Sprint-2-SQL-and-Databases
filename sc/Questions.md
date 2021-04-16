#############################################
#           Questions and Answers           #
############################################

## In Northwind Database, what is the type of relationship between Employee and Territory tables?

Employees to Territories have a "one to many relationship". From what I saw, in the
"EmployeeTerritory" table, there are no duplicate territory ID's, but multiple
territory Id's were assigned to the same employee ID. Thus one employee to many
territories properly describes the relationship.

## What is a situtation where a document store (MongoDB) is appropriate? When is it not?

Document stores are really great at not storing duplicate information. In traditional SQL databases, there are multiple tables which must be related by a common column, (typically an ID key which is primary in one, foreign in another). Because of the lack of a table structure, entries aren't necessarily the same size and so there's an even further reduction in information. As such, it scales really well because it avoids this duplicate information. They are appropriate when you want to search for data dynamically. This flexibility is the main shortcoming because new documents don't need to match datatypes, so it can get messy or lost when handled by lazy data angineers.

## What is NewSQL and what is it trying to achieve?

NewSQL is proposing to be the "best of both worlds" between document-oriented and relational databases. It seeks to be scalable and flexible like document stores while maintaining ACID compliance of traditional relational database systems. NewSQL seeks to be familiar in syntax with options like "SELECT" and familiar clauses "GROUP BY", "ORDER BY", etc. 
