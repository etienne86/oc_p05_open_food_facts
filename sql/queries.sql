-- This file contains all SQL requests to be executed first,
-- as administrator (user 'root'), to create a user ('pur_guest'),
-- a database ('pur_beurre_05'), and privileges for this user on this database.


-- create a user
CREATE USER 'pur_guest'@'localhost'; -- password is useless


-- create the database pur_beurre_05
CREATE DATABASE pur_beurre_05 CHARACTER SET 'utf8mb4';
USE pur_beurre_05;


-- assign rights to this user on the database
GRANT ALL PRIVILEGES ON pur_beurre_05.* TO 'pur_guest'@'localhost';
