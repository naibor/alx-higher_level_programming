-- created database and table
-- description: cities
--	id INT unique,auto generate, cant be null, primary key
--	state_id INT cant be null foreign key reference to id of state table
--	name VARCHAR can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTs cities(id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY (id), FOREIGN KEY(state_id) REFERENCES state(id));
