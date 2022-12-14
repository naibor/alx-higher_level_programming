-- Creates the database 'hbtn_0d_2' and user 'user_0d_2'
-- User shoulld only have select privillages

CREATE DATABASE IF NOT EXIST 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH 'user_0d_2_pwd';
-- Privilages
GRANT USAGE ON * . * TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2` . * TO 'user_0d_2'@'localhost';
