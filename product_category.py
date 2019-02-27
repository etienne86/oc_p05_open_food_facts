#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'ProductCategory' class."""


class ProductCategory:
    """This class is used to link products and categories."""

    def __init__(self, product_code, category_name):
        """This special method is the class constructor."""
        self.product_code = product_code # type is int
        self.category_name = category_name # type is string
