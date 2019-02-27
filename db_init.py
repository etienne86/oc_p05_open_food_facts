#! /usr/bin/env python3
# coding: utf-8

"""Please execute this module to initiate the database pur_beurre_05"""

import mysql.connector


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
            product_name VARCHAR(1000) NOT NULL,
            nutrition_grade_fr VARCHAR(1),
            nutrition_score_fr_100g INT,
            nutrition_score_uk_100g INT,
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
                    id INT UNSIGNED NOT NULL,
                    substitute_id INT UNSIGNED NOT NULL,
                    product_id INT UNSIGNED NOT NULL,
                    PRIMARY KEY (id)
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


def main():
    """docstring"""
    
    # We connect to the database pur_beurre_05
    connexion = mysql.connector.connect(host="localhost",
                                        user="pur_guest",
                                        database="pur_beurre_05"
                                        )

    # We initiate a cursor
    cursor = connexion.cursor()
    
    # We create the tables
    for sql_request in SQL_TABLES_CREATIONS:
        cursor.execute(sql_request)

    # We add the foreign keys
    for sql_request in SQL_FK:
        cursor.execute(sql_request)

    # We close the connexion to the database
    connexion.close()


if __name__ == "__main__":
    main()
