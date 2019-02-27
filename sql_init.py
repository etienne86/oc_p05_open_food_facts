#! /usr/bin/env python3
# coding: utf-8

"""This module contains the strings used to initiate the database."""


SQL_TABLES_CREATIONS = [
    """
    CREATE TABLE Store (
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(1000) NOT NULL,
            PRIMARY KEY (id)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE Category (
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(1000) NOT NULL,
            PRIMARY KEY (id)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE Product (
            code INT UNSIGNED NOT NULL,
            product_name VARCHAR(1000) NOT NULL,
            nutrition_grade_fr VARCHAR(1),
            nutrition_score_fr_100g INT,
            nutrition_score_uk_100g INT,
            url VARCHAR(1000) NOT NULL,
            PRIMARY KEY (code)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE ProductCategory (
                    product_code INT UNSIGNED NOT NULL,
                    category_name INT UNSIGNED NOT NULL,
                    PRIMARY KEY (product_code, category_name)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE ProductStore (
                    product_code INT UNSIGNED NOT NULL,
                    store_name INT UNSIGNED NOT NULL,
                    PRIMARY KEY (product_code, store_name)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE SavedProduct (
                    substitute_code INT UNSIGNED NOT NULL,
                    product_code INT UNSIGNED NOT NULL,
                    PRIMARY KEY (substitute_code, product_code)
    )
    ENGINE=INNODB;
    """
]

SQL_FK = [
    """
    ALTER TABLE ProductStore
    ADD CONSTRAINT store_product_store_fk
    FOREIGN KEY (store_name)
    REFERENCES Store (name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE ProductCategory
    ADD CONSTRAINT category_product_category_fk
    FOREIGN KEY (category_name)
    REFERENCES Category (name)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE SavedProduct
    ADD CONSTRAINT product_saved_product_fk
    FOREIGN KEY (product_code)
    REFERENCES Product (code)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE ProductStore
    ADD CONSTRAINT product_product_store_fk
    FOREIGN KEY (product_code)
    REFERENCES Product (code)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE ProductCategory
    ADD CONSTRAINT product_product_category_fk
    FOREIGN KEY (product_code)
    REFERENCES Product (code)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE SavedProduct
    ADD CONSTRAINT product_saved_product_fk1
    FOREIGN KEY (substitute_code)
    REFERENCES Product (code)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """
]
