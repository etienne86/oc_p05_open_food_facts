#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Category' class."""


import random

class Category:
    """This class is used to represent the categories,
    used to classify the products."""

    CATEGORIES_LIST = [
        "desserts",
        "eaux",
        "fromages",
        "legumes",
        "pains",
        "pizzas",
        "poissons",
        "riz",
        "viandes",
    ]

    def __init__(self, name):
        """This special method is the class constructor."""
        self.name = name # type is str

    def add_category_to_db(self, connection):
        """This method is responsible for adding
        a category to the database.
        """
        # initiate a cursor
        cursor = connection.cursor()
        # check if the category already exists in database
        cursor.execute("""SELECT name FROM Category
                          WHERE name = %s""", (self.name, ))
        rows = cursor.fetchall()
        if not rows:
            # insert data
            cursor.execute("""INSERT INTO Category (name)
                              VALUES (%(name)s)""", self.__dict__)
            # commit the changes
            connection.commit()

    def best_prod(self, connection):
        """This method is responsible for determining the best product
        inside the category, considering nutrition data.
        """
        best_nutri_score_fr = -999
        # initiate a cursor
        cursor = connection.cursor()
        # determine the best nutri-score in the category
        cursor.execute("""SELECT c.name,
                                 MIN(p.nutrition_score_fr_100g) AS mini
                          FROM Category AS c
                          LEFT JOIN ProductCategory AS pc
                          ON c.id = pc.category_id
                          LEFT JOIN Product AS p
                          ON p.id = pc.product_id
                          WHERE c.name = %s""", (self.name, ))
        rows = cursor.fetchall()
        if rows:
            best_nutri_score_fr = rows[0][1]
        # select lines with the best nutriscore_fr
        cursor.execute("""SELECT c.name, p.id, p.code, p.product_name,
                                 p.nutrition_grade_fr,
                                 p.nutrition_score_fr_100g, p.url
                          FROM Product AS p
                          LEFT JOIN ProductCategory AS pc
                          ON p.id = pc.product_id
                          LEFT JOIN Category AS c
                          ON c.id = pc.category_id
                          WHERE p.nutrition_score_fr_100g = %s
                            AND c.name = %s""",
                          (best_nutri_score_fr, self.name))
        rows = cursor.fetchall()
        # there has to be at least one line in rows
        rand = random.randint(0, len(rows) - 1)
        # select and return a random product among the best ones
        return rows[rand] # type is tuple
        # (Category.name, Product.id, Product.code, Product.name,
        #  Product.nutrition_grade_fr, Product.nutrition_score_fr_100g,
        #  Product.url)

    def get_url_1k_products(self):
        """This method is responsible for supplying the search url,
        which displays 1000 products, based on the category name."""
        if self.name in Category.CATEGORIES_LIST:
            res = "https://fr.openfoodfacts.org/cgi/search.pl?" \
                + "action=process&tagtype_0=categories" \
                + "&tag_contains_0=contains&tag_0=" \
                + self.name + "&page_size=1000&json=1"
            return res
        else:
            return ""