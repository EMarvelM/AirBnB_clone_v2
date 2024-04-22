-- create database and script should not fail if already created
CREATE DATABASE IF NOT EXITS hbnb_test_db;
-- create a new user
CREATE USER 'hbnb_test'@'localhost' IDENTIFY BY 'hbnb_test_pwd';
-- grant priviledge
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;


