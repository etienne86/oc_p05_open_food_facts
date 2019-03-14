#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'SavedProduct' class."""


from datetime import datetime


class SavedProduct:
    """This class is used to represent the products (food)."""

    SAVED_LIST = []

    def __init__(self, prod_out, prod_in):
        """This special method is the class constructor."""
        self.prod_out = prod_out # type is <class 'Product'>
        self.prod_in = prod_in # type is <class 'Product'>
        self.date = str(datetime.now())[0:10]

    def add_saved_prod_to_db(self, connection, sub_id, prod_id):
        """This method is responsible for adding
        a saved product to the database.
        """
        # initiate a cursor
        cursor = connection.cursor()
        # check if the category already exists in database
        cursor.execute("""SELECT substitute_id, product_id FROM SavedProduct
                          WHERE substitute_id = %s AND product_id = %s""",
                          (sub_id, prod_id, ))
        rows = cursor.fetchall()
        if not rows:
            # insert data
            cursor.execute("""INSERT INTO SavedProduct
                              (substitute_id, product_id)
                              VALUES (%s, %s)""", (sub_id, prod_id, ))
            # commit the changes
            connection.commit()
            # confirm to user
            print("Votre substitut est bien enregistré !")
        else:
            print("Ce remplacement de produit est déjà enregistré.")

    def rm_saved_prod_from_db(self):
        """This method is responsible for removing
        a saved product from the database.
        """
        pass pass
