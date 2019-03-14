#! /usr/bin/env python3
# coding: utf-8

"""
Please execute this module to replace your foodstuffs
and register your substitutes.
"""


# import re

import mysql.connector
# import requests

#from category import Category
from menu import Menu
# from product import Product
# from store import Store


def main():
    """doctrinsg"""
    # connect to the database pur_beurre_05
    connection = mysql.connector.connect(host="localhost",
                                         user="pur_guest",
                                         database="pur_beurre_05"
                                        )
    # initiate a menu instance
    crt_menu = Menu()
    # run as long as the user does not ask to quit
    while crt_menu.status:
        if crt_menu.status == ["main_menu"]:
            crt_menu.display_main()
        elif crt_menu.status == ["main_menu", "categ_list"]:
            crt_menu.display_categ(connection)
        elif crt_menu.status == ["main_menu", "categ_list", "prod_list"]:
            crt_menu.display_prod(connection)
        elif crt_menu.status == ["main_menu", "categ_list",
                                 "prod_list", "suggested_sub"]:
            crt_menu.display_suggested_sub()
        elif crt_menu.status == ["my_subs"]:
            crt_menu.display_my_subs()
        elif crt_menu.status == ["my_subs", "sub_to_del"]:
            crt_menu.display_sub_to_del()
    # close the connection to the database
    connection.close()
    print("\nA bientôt !\n")

if __name__ == "__main__":
    main()










