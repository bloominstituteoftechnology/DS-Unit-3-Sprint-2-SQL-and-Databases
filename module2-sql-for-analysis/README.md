# Sprint 2 Module 2 -

## Learning Objectives

* Deploy and use a simple PostgreSQL database
* Create a data pipeline with SQL

## Before Lecture

Sign up for a free [ElephantSQL](https://www.elephantsql.com/) account. This will allow you to run a "cloud" PostgreSQL instance (20mb). If you wish, you may also install [PostgreSQL](https://www.postgresql.org/) locally, which facilitates larger databases, but is not necessary for our daily tasks.

You can also install [pgAdmin](https://www.pgadmin.org/), which (like the DB Browser for SQLite) lets you connect to, explore, and query databases using a Graphical User Interface (GUI) tool. This is optional, but can be really helpful when connecting to the database and getting a better visual representation of the DB.

## Guided Project

[See guided-project.md](https://github.com/BloomInstituteOfTechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/guided-project.md)

## Assignment

[See assignment.md](https://github.com/BloomInstituteOfTechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/assignment.md)

## Stretch Goals

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

## Resources

PostgreSQL is a truly powerful production database - explore the [official
documentation](https://www.postgresql.org/docs/) as well as larger hosted
offerings such as [Amazon RDS](https://aws.amazon.com/rds/postgresql/).
