-- We create a user
CREATE USER 'pur_guest'@'localhost'; -- password is useless


-- We create the database pur_beurre_05
CREATE DATABASE pur_beurre_05 CHARACTER SET 'utf8mb4';
USE pur_beurre_05;


-- We assign rights to this user on the database
GRANT ALL PRIVILEGES ON pur_beurre_05.* TO 'pur_guest'@'localhost';



INSERT INTO Product (
    product_name,
    nutrition_grade_fr,
    nutrition_score_fr_100g,
    nutrition_score_uk_100g,
    url
    )
VALUES (
    "eau plate",
    "a",
    -1,
    -1,
    "https://www.google.com/"
    );

