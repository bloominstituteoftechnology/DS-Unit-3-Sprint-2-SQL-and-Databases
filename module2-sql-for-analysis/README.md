## **Learning Objectives**
* Deploy and use a simple PostgreSQL database
* Create a data pipeline with SQL

## **Before Lecture**
Sign up for a free [ElephantSQL](https://www.elephantsql.com/) account. This will allow you to run a "cloud" PostgreSQL instance (20mb). If you wish, you may also install [PostgreSQL](https://www.postgresql.org/) locally, which facilitates larger databases, but is not necessary for our daily tasks.

You can also install [pgAdmin](https://www.pgadmin.org/), which (like the DB Browser for SQLite) lets you connect to, explore, and query databases using a Graphical User Interface (GUI) tool. This is optional, but can be pretty important when connecting to the database and getting a better visual representation of the DB.


## **Live Lecture Task**
Yesterday we used a simple local workflow with SQLite - today, we'll work on inserting the same RPG data into a more production-style PostgreSQL database running on a server. We will use [psycopg](http://initd.org/psycopg/), a Python library for connecting to PostgreSQL, and specifically we will install [psycopg2-binary](https://pypi.org/project/psycopg2-binary/).

Once we get the data inserted, we will continue exploring and querying like we did  yesterday, first answering the same questions and then going deeper. We'll also explore some of the specific functions that are different in PostgreSQL than SQLite.


## Assignment

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
 
## Resources and Stretch Goals

#### Stretch: 
Try to install and use the actual [psycopg2](https://pypi.org/project/psycopg2/)
package (as opposed to `psycop2-binary`). This builds from source, so there are
[prerequisites](http://initd.org/psycopg/docs/install.html#install-from-source)
you'll need. This may be good to do inside a container!

Want to try larger PostgreSQL databases? Check out [these sample
databases](https://community.embarcadero.com/article/articles-database/1076-top-3-sample-databases-for-postgresql),
but note you'll probably need a local installation of PostgreSQL to be able to
use them.

You can revisit [Django](https://docs.djangoproject.com/en/2.1/intro/), which was briefly introduced
yesterday. This is a complete stretch goal (i.e. it's not a core Data Science
skill and is OK if you don't get to it at all), but it is a powerful and
widely-used web application framework. Also, the Django ORM can connect to a
variety of SQL backends, and a very typical setup is to use SQLite for (initial)
local development but PostgreSQL for deployment.


#### Resources: 
PostgreSQL is a truly powerful production database - explore the [official
documentation](https://www.postgresql.org/docs/) as well as larger hosted
offerings such as [Amazon RDS](https://aws.amazon.com/rds/postgresql/).
