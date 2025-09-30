-- MySQL setup script for AirBnB clone v2 (development)
-- Creates database and grants per project requirements.

-- 1) Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- 2) Create user if not exists (local only)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- 3) Grant all privileges on hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- 4) Grant SELECT on performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- 5) Apply privilege changes
FLUSH PRIVILEGES;


