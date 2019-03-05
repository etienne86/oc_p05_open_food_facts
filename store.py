#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Store' class."""


class Store:
    """This class is used to represent the stores,
    where the products could be purchased."""

    def __init__(self, name):
        """This special method is the class constructor."""
        self.name = name # type is string

    def add_store_to_db(self, connexion):
        """This method is responsible for adding
        a store to the database, if not already existing.
        """

        # initiate a cursor
        cursor = connexion.cursor()
        # check if the store already exists in database
        cursor.execute("""SELECT name FROM Store
                          WHERE name = %s""", (self.name, ))
        rows = cursor.fetchall()
        if not rows:
            # insert data
            cursor.execute("""INSERT INTO Store (name)
                              VALUES (%(name)s)""", self.__dict__)
            # commit the changes
            connexion.commit()  
