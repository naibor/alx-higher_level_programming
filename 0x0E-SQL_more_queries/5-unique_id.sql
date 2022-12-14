-- Creates a table
-- description: unique_id
--	id (INT) default 1, must be unique
--	name VARCHAR

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256)); 
