#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Category' class."""


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
        self.name = name # type is string

    def add_category_to_db(self, connexion):
        """This method is responsible for adding
        a category to the database.
        """
        # initiate a cursor
        cursor = connexion.cursor()
        # check if the category already exists in database
        cursor.execute("""SELECT name FROM Category
                          WHERE name = %s""", (self.name, ))
        rows = cursor.fetchall()
        if not rows:
            # insert data
            cursor.execute("""INSERT INTO Category (name)
                              VALUES (%(name)s)""", self.__dict__)
            # commit the changes
            connexion.commit()

    def get_url_1k_products(self):
        """This method is responsible for supplying the search url,
        which displays 1000 products, based on the category name."""
        if self.name in Category.CATEGORIES_LIST:
            return f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={self.name}&page_size=1000&json=1"
                    #https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=desserts&page_size=20&json=1
        else:
            return ""