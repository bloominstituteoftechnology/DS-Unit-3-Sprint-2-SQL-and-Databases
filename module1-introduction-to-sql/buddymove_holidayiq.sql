/* Row count */ 
select count(*) from "buddymove_holidayiq.sqlite3";

/* How many users made at least 100 nature and at least 100 shopping category reviews? */
select count("User ID") from "buddymove_holidayiq.sqlite3" where Nature >= 100 and Shopping >= 100;

/*(Stretch) find average number of reviews for each category */
select avg(Sports), avg(Religious), avg(Nature), avg(Theatre), avg(Shopping), avg(Picnic) from "buddymove_holidayiq.sqlite3";
