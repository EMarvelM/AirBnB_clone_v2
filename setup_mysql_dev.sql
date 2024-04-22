-- Create project testing database with the name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating new user named: hbnb_test with all privileges on the db hbnb_dev_db
-- with the password: hbnb_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting the SELECT privilege for the user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;

-- Granting all privileges to the new user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;

