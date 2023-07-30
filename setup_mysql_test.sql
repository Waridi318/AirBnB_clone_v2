-- create a hbnb_dev_test database and hbnb_test user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
USE perfomance_schema;
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
