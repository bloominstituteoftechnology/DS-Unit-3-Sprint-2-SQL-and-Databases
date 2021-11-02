# Guided Project Walkthrough

Yesterday we used a simple local workflow with SQLite - today, we'll work on inserting the same RPG data into a more production-style PostgreSQL database running on a server. We will use [psycopg](http://initd.org/psycopg/), a Python library for connecting to PostgreSQL, and specifically we will install [psycopg2-binary](https://pypi.org/project/psycopg2-binary/).

Once we get the data inserted, we will continue exploring and querying like we did  yesterday, first answering the same questions and then going deeper. We'll also explore some of the specific functions that are different in PostgreSQL than SQLite.
