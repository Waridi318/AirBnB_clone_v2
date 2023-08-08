-- create a hbnb_dev_db database and hbnb_dev user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
CREATE DATABASE IF NOT EXISTS perfomance_schema;
USE perfomance_schema;
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
