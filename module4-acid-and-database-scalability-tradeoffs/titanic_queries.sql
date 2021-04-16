/* How many passengers Survived/ Died on the Titanic? */
-- two possibilities:
select sum(survived) as survived, count(survived) - sum(survived)  as died from "titanic.sqlite3";

select survived, count(*) as "count" from "titanic.sqlite3" group by survived;

/* How many passengers were in each class? */
select pclass, count(pclass) as "count" from "titanic.sqlite3" group by pclass;


/* How many passengers died/survived within each class? */
select pclass, survived, count(survived) as "count" from "titanic.sqlite3" group by pclass,survived;

/* What was the average age of survivors vs nonsurvivors? */
select survived, avg(age) as "Average Age" from "titanic.sqlite3" group by survived;

/* What was the average age of each passenger class? */
select pclass, avg(age ) as "Average Age" from "titanic.sqlite3" group by pclass;


/*What was the average fare by passenger class? By survival?*/
select pclass, avg(fare) as "average fare" from "titanic.sqlite3" group by pclass;
select survived, avg(fare) as "average fare" from "titanic.sqlite3" group by survived;

/*How many siblings/spouses aboard on average, by passenger class? By survival*/
select pclass, avg("Siblings/Spouses Aboard") from "titanic.sqlite3" group by pclass;
select survived, avg("Siblings/Spouses Aboard") from "titanic.sqlite3" group by survived;

/*How many parents/children aboard on average, by passenger class? By survival*/
select pclass, avg("parents/children aboard") from "titanic.sqlite3" group by pclass;
select survived, avg("parents/children aboard") from "titanic.sqlite3" group by survived;


/* Do any passengers have the same name? */
select name, count(*) "count" from "titanic.sqlite3" group by name order by "count" DESC limit 3;
--no. Top results only show a count of 1
-- This wasn't asked for, but if we consider the same first name:
/*Do any passengers have the same name*/


select substr(
		ltrim(substr(replace(replace(name,'Master','Mr'),'.',' '),5,50)),
		0,
		instr(ltrim(substr(replace(replace(name,'Master','Mr'),'.',' '),5,50)),' ')) as first_name, count(*) as occurence from "titanic.sqlite3" group by first_name order by occurence desc;

/* first few outputs
William	48
John	30
Thomas	18
Charles	16
George	16
Henry	15*/
