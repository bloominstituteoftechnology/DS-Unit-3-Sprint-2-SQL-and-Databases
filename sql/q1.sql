-- get the character_id for the characterscreators_characters table
-- and count the number of unique id's there are

SELECT
	COUNT(DISTINCT character_id) as char_count
FROM charactercreator_character
ORDER BY 1
