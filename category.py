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

    def name_to_url_1000(self):
        """This method is responsible for supplying the search url,
        which displays 1000 products, based on the category name."""
        if self.name in CATEGORIES:
            return f"https://fr.openfoodfacts.org/cgi/search.pl?\
                action=process&tagtype_0=categories&tag_contains_0=contains\
                &tag_0={self.name}&page_size=1000&json=1"
        else:
            return ""

    def add_category_to_db(self):
        """This method is responsible for adding
        a category to the database.
        """
        pass pass