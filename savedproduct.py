#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'SavedProduct' class."""


class SavedProduct:
    """This class is used to represent the records (saved products)."""

    def __init__(self, prod_id, sub_id):
        """This special method is the class constructor."""
        self.prod_id = prod_id # type is int
        self.sub_id = sub_id # type is int
        self.date = "" # type is str

    def add_saved_prod_to_db(self, connection):
        """This method is responsible for adding
        a saved product to the database.
        """
        # initiate a cursor
        cursor = connection.cursor()
        # check if the couple (product, substitute) already exists in database
        cursor.execute("""SELECT product_id, substitute_id
                          FROM SavedProduct
                          WHERE product_id = %s AND substitute_id = %s""",
                       (self.prod_id, self.sub_id)
                      )
        rows = cursor.fetchall() # type is list of zero, or one, tuple
        if not rows:
            # insert data
            cursor.execute("""INSERT INTO SavedProduct
                              (product_id, substitute_id, save_date)
                              VALUES (%s, %s, CURDATE())""",
                           (self.prod_id, self.sub_id)
                          )
            # commit the changes
            connection.commit()
            # confirm to user
            print("\nVotre substitut est bien enregistré !\n")
            # no need to update self.date here
            # self.date is used only if this substitution is already saved
        else:
            # remind the date of instance
            cursor.execute("""SELECT product_id, substitute_id,
                                     DATE_FORMAT(save_date, "%d/%m/%Y")
                              FROM SavedProduct
                              WHERE product_id = %s AND substitute_id = %s""",
                           (self.prod_id, self.sub_id)
                          )
            date_row = cursor.fetchall() # type is list of tuples
            self.date = date_row[0][2]
            print(f"\nL'enregistrement a déjà été effectué le {self.date}.\n")
