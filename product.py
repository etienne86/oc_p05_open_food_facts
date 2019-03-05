#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Product' class."""


class Product:
    """This class is used to represent the products (food)."""

    def __init__(self):
        """This special method is the class constructor."""
        self.code = 0 # type is int
        self.product_name = "" # type is string
        self.nutrition_grade_fr = "" # type is string
        self.nutrition_score_fr_100g = -999 # type is int
        self.nutrition_score_uk_100g = -999 # type is int
        self.url = "" # type is string
        self.countries = "" # type is string

    def add_product_category_to_db(self, category_name, connexion):
        """This method is responsible for inserting a record,
        in table ProductCategory, to link a product and a category.
        """
        # initiate a cursor
        cursor = connexion.cursor()
        # get category_id from category_name
        cursor.execute("""SELECT id FROM Category
                          WHERE name = %s""", (category_name, ))
        categ_row = cursor.fetchall()
        if categ_row:
            category_id = categ_row[0][0]
        # get product_id from product code
        cursor.execute("""SELECT id FROM Product
                          WHERE code = %(code)s""", self.__dict__)
        prod_row = cursor.fetchall()
        if prod_row:
            product_id = prod_row[0][0]
        if categ_row and prod_row:    
            # check if the couple (product, category) already exists
            cursor.execute("""SELECT product_id, category_id
                              FROM ProductCategory
                              WHERE product_id = %s AND category_id = %s""",
                              (product_id, category_id)
                          )
            prod_categ_row = cursor.fetchall()
            if not prod_categ_row:
                # insert data
                cursor.execute("""INSERT INTO ProductCategory (product_id,
                                                               category_id)
                                  VALUES (%s, %s)""", (product_id,
                                                       category_id))
                # commit the changes
                connexion.commit()

    def add_product_store_to_db(self, store_name, connexion):
        """This method is responsible for inserting a record,
        in table ProductStore, to link a product and a store.
        """
        # initiate a cursor
        cursor = connexion.cursor()
        # get store_id from store_name
        cursor.execute("""SELECT id FROM Store
                          WHERE name = %s""", (store_name, ))
        store_row = cursor.fetchall()
        if store_row:
            store_id = store_row[0][0]
        # get product_id from product code
        cursor.execute("""SELECT id FROM Product
                          WHERE code = %(code)s""", self.__dict__)
        prod_row = cursor.fetchall()
        if prod_row:
            product_id = prod_row[0][0]
        if store_row and prod_row:
            # check if the couple (product, store) already exists
            cursor.execute("""SELECT product_id, store_id FROM ProductStore
                              WHERE product_id = %s AND store_id = %s""",
                              (product_id, store_id)
                          )
            prod_store_row = cursor.fetchall()
            if not prod_store_row:
                # insert data
                cursor.execute("""INSERT INTO ProductStore (product_id,
                                                            store_id)
                                  VALUES (%s, %s)""", (product_id,
                                                       store_id))
                # commit the changes
                connexion.commit()

    def add_product_to_db(self, connexion):
        """This method is responsible for adding
        a product to the database.
        """
        # initiate a cursor
        cursor = connexion.cursor()
        # check if the product already exists in database
        cursor.execute("""SELECT code FROM Product
                          WHERE code = %s""", (self.code, ))
        rows = cursor.fetchall()
        if not rows and (self.code < 10**14): # code has at most 13 digits
            # insert data
            cursor.execute("""INSERT INTO Product (code,
                                                   product_name,
                                                   nutrition_grade_fr,
                                                   nutrition_score_fr_100g,
                                                   nutrition_score_uk_100g,
                                                   url)
                              VALUES (%(code)s,
                                      %(product_name)s,
                                      %(nutrition_grade_fr)s,
                                      %(nutrition_score_fr_100g)s,
                                      %(nutrition_score_uk_100g)s,
                                      %(url)s)
                           """, self.__dict__)
            # commit the changes
            connexion.commit()
