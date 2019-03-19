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
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            code BIGINT UNSIGNED NOT NULL,
            product_name VARCHAR(1000) NOT NULL,
            nutrition_grade_fr VARCHAR(1) NOT NULL,
            nutrition_score_fr_100g INT NOT NULL,
            url VARCHAR(1000) NOT NULL,
            PRIMARY KEY (id)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE ProductCategory (
                    product_id INT UNSIGNED NOT NULL,
                    category_id INT UNSIGNED NOT NULL,
                    PRIMARY KEY (product_id, category_id)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE ProductStore (
                    product_id INT UNSIGNED NOT NULL,
                    store_id INT UNSIGNED NOT NULL,
                    PRIMARY KEY (product_id, store_id)
    )
    ENGINE=INNODB;
    """,
    """
    CREATE TABLE SavedProduct (
                    product_id INT UNSIGNED NOT NULL,
                    substitute_id INT UNSIGNED NOT NULL,
                    save_date DATE NOT NULL,
                    PRIMARY KEY (product_id, substitute_id)
    )
    ENGINE=INNODB;
    """
]

SQL_FK = [
    """
    ALTER TABLE ProductStore
    ADD CONSTRAINT store_product_store_fk
    FOREIGN KEY (store_id)
    REFERENCES Store (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE ProductCategory
    ADD CONSTRAINT category_product_category_fk
    FOREIGN KEY (category_id)
    REFERENCES Category (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE SavedProduct
    ADD CONSTRAINT product_saved_product_fk
    FOREIGN KEY (product_id)
    REFERENCES Product (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE ProductStore
    ADD CONSTRAINT product_product_store_fk
    FOREIGN KEY (product_id)
    REFERENCES Product (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE ProductCategory
    ADD CONSTRAINT product_product_category_fk
    FOREIGN KEY (product_id)
    REFERENCES Product (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """,
    """
    ALTER TABLE SavedProduct
    ADD CONSTRAINT product_saved_product_fk1
    FOREIGN KEY (substitute_id)
    REFERENCES Product (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    """
]
