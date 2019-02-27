#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'ProductStore' class."""


class ProductStore:
    """This class is used to link products and stores."""

    def __init__(self, product_code, store_name):
        """This special method is the class constructor."""
        self.product_code = product_code # type is int
        self.store_name = store_name # type is string

    def sql_insert(self):
        """This method is responsible for inserting a new line in the database,
        to link a product and a store.
        """
        pass pass