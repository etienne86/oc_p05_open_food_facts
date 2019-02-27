#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Product' class."""


class Product:
    """This class is used to represent the products (food)."""

PRODUCT_ATTRIBUTES = [
    "code",
    "product_name",
    "nutrition_score_fr_100g",
    "nutrition_grade_fr",
    "nutrition_score_uk_100g",
    "url",
]

    def __init__(self):
        """This special method is the class constructor."""
        self.code = 0 # type is int
        self.product_name = "" # type is string
        self.nutrition_grade_fr = "" # type is string
        self.nutrition_score_fr_100g = -999 # type is int
        self.nutrition_score_uk_100g = -999 # type is int
        self.url = "" # type is string
        self.countries = "" # type is string

    def abc(self):
        """This method is responsible for xyz."""
        pass pass
