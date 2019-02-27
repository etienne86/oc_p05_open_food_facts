#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Store' class."""


class Store:
    """This class is used to represent the stores,
    where the products could be purchased."""

STORES_LIST = []

    def __new__(cls, name):
        if name not in STORES_LIST:
            STORES_LIST.append(name)
        return object.__new__(cls, name)

    def __init__(self, name):
        """This special method is the class constructor."""
        self.name = name # type is string
        self.codes = [] # type is list (of int)

    def add_code(self, code):
        """This method is responsible for adding
        a product code linked to the store."""
        self.codes.append(code)
