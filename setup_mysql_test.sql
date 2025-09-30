-- MySQL setup script for AirBnB clone v2 (test)
-- Creates test database and grants per project requirements.

-- 1) Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- 2) Create user if not exists (local only)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- 3) Grant all privileges on hbnb_test_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- 4) Grant SELECT on performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- 5) Apply privilege changes
FLUSH PRIVILEGES;


