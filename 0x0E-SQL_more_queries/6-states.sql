-- Creates a database and tables
-- description: hbtn_0d_usa
-- 	table: states
--	 id (INT) unique, auto genenrated can't be null
--	 name (VARCHAR) cant be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT UNIQUE, name VARCHAR(256) NOT NULL primary key (id))

