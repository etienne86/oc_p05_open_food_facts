#! /usr/bin/env python3
# coding: utf-8

"""Please execute this module to initiate the database pur_beurre_05.
Pre-requisites:
- the database 'pur_beurre_05' has to be created
- all privileges have to be granted to user 'pur_guest' on 'pur_beurre_05'
"""


import mysql.connector

import sql_db_init


def main():
    """docstring"""

    # connect to the database pur_beurre_05
    connection = mysql.connector.connect(host="localhost",
                                 user="pur_guest",
                                 database="pur_beurre_05"
                                )

    # initiate a cursor
    cursor = connection.cursor()

    # create the tables
    for sql_request in sql_db_init.SQL_TABLES_CREATIONS:
        cursor.execute(sql_request)

    # add the foreign keys
    for sql_request in sql_db_init.SQL_FK:
        cursor.execute(sql_request)

    # close the connection to the database
    connection.close()


if __name__ == "__main__":
    main()
