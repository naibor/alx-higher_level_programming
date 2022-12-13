-- list all records of table
-- Don't list rows without name
-- Display score then name in decending order

SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
