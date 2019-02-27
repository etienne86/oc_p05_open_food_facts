#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Store' class."""


class Store:
    """This class is used to represent the stores,
    where the products could be purchased."""

STORES_LIST = []

    def __init__(self, name):
        """This special method is the class constructor."""
        self.name = name # type is string
        self.codes = [] # type is list (of int)

    def add_store_to_db(self):
        """This method is responsible for adding
        a store to the database, if not already existing.
        """
        if self.name not in STORES_LIST:
            STORES_LIST.append(self.name)
