#! /usr/bin/env python3
# coding: utf-8

"""Please execute this module to initiate the database pur_beurre_05.
Pre-requisites:
- the database 'pur_beurre_05' has to be created
- all privileges have to be granted to user 'pur_guest' on 'pur_beurre_05'
"""


import mysql.connector

from sql_db_init import *


def main():
    """docstring"""
    
    # We connect to the database pur_beurre_05
    connexion = mysql.connector.connect(host="localhost",
                                        user="pur_guest",
                                        database="pur_beurre_05"
                                        )

    # We initiate a cursor
    cursor = connexion.cursor()
    
    # We create the tables
    for sql_request in SQL_TABLES_CREATIONS:
        cursor.execute(sql_request)

    # We add the foreign keys
    for sql_request in SQL_FK:
        cursor.execute(sql_request)

    # We close the connexion to the database
    connexion.close()


if __name__ == "__main__":
    main()
