#! /usr/bin/env python3
# coding: utf-8

"""
Please execute this module to replace your foodstuffs
and save your substitutes.
Warning: before executing this module,
you should have executed first db_init.py.
"""


import mysql.connector

from menu import Menu


def main():
    """This function is the main function to be executed to run the program."""
    print("\nBienvenue dans ce programme de remplacement d'aliments !",
          "\nLes données sont issues du site d'OpenFoodFacts.")
    # connect to the database pur_beurre_05
    connection = mysql.connector.connect(host="localhost",
                                         user="pur_guest",
                                         database="pur_beurre_05"
                                        )
    prod_id = categ_id = 0
    # create a menu instance
    crt_menu = Menu()
    # run as long as the user does not ask to quit
    while crt_menu.status:
        if crt_menu.status == ["main_menu"]:
            crt_menu.display_main()
        elif crt_menu.status == ["main_menu", "categ_list"]:
            crt_menu.display_categ(connection)
        elif crt_menu.status == ["main_menu", "categ_list", "prod_list"]:
            (prod_id, categ_id) = crt_menu.display_prod(connection)
        elif crt_menu.status == ["main_menu", "categ_list",
                                 "prod_list", "suggested_sub"]:
            crt_menu.display_suggested_sub(connection, prod_id, categ_id)
        elif crt_menu.status == ["main_menu", "my_subs"]:
            crt_menu.display_my_subs(connection)
        else:
            raise ValueError(crt_menu.status)
    # close the connection to the database
    connection.close()
    print("\nA bientôt !\n")

if __name__ == "__main__":
    main()
