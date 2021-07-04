In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

  - The type of relationship between the 'Employee' and 'Territory'
    tables can be described as many-to-one. This means that many 
    employees can belong to a single territory. For the most part,
    the opposite is untru in that one person doesn't typically 
    live in multiple territories.

What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

    - MongoDB is usefull in scenarios where the schema can be flexible.
    This is especially usefull in start-up type scenarios where a team
    can prototype a project quickly. MongoDB wouldn't be appropriate
    for more secure types of databases that require strict adherance to
    a standard and rigid implementation: like a bank or public records
    office.

What is "NewSQL", and what is it trying to achieve?

    - NewSQl is attempting to bridge the gap between SQL databases
    and NoSQL databases. It relaxes some constraints on standard
    practices such as availability and consistency in order to achieve
    a faster transaction times with large scale databases. NewSQL still 
    lives in a space of innovation, spured by the growth of horizontal
    scalability.