-- setting up a new table
/*CREATE TABLE IF NOT EXISTS test_table
(
	id SERIAL PRIMARY KEY,
	name varchar(40) NOT NULL,
	data JSONB
);
*/

--inserting information into a  table
/*
INSERT INTO test_table (name,data) VALUES
('A row name',NULL),
('another row with json','{"a":1,"b":2,"c":3}'::JSONB);
*/

--goal update the name value of recors with an id = 2
/*
UPDATE test_table
SET name =  'new name'
where id=2;
*/

