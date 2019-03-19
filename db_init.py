#! /usr/bin/env python3
# coding: utf-8

"""Please execute this module to build
and fill in the database 'pur_beurre_05'.
Pre-requisites:
- the database 'pur_beurre_05' has to be created
- all privileges have to be granted to user 'pur_guest' on 'pur_beurre_05'
"""


import re

import mysql.connector
import requests

from category import Category
from product import Product
from store import Store
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
    ## part 1: initialize the database
    # create the tables
    for sql_request in sql_db_init.SQL_TABLES_CREATIONS:
        cursor.execute(sql_request)
    # add the foreign keys
    for sql_request in sql_db_init.SQL_FK:
        cursor.execute(sql_request)
    ## part 2: fill in the database tables with products, categories and stores
    # iterate on each pre-selected category
    for categ_name in Category.CATEGORIES_LIST:
        categ = Category(categ_name)
        # add the category to the database
        categ.add_category_to_db(connection)
        # execute the HTTP request to get products with API
        categ_1k = requests.get(categ.get_url_1k_products())
        categ_1k_dict = categ_1k.json()
        if (categ_1k.status_code == 200) and (categ_1k_dict["count"]):
            api_return = categ_1k.json() # type is dict
            products_list = api_return["products"] # type is list of dict
            # iterate on each product
            for item in products_list: # type is dict
                # initiate a new instance of product
                prod = Product()
                # filter on:
                # - products containing "France" in the list of countries
                # - products with 'nutrition_grade_fr' and 'code' completed
                regexp = "(.*)[Ff]rance(.*)"
                if (re.match(regexp, item["countries"]) is not None) \
                        and ("code" in item.keys()) \
                        and ("nutrition_grade_fr" in item.keys()):
                    # set the product attributes
                    prod.code = int(item["code"])
                    prod.product_name = item["product_name"]
                    prod.nutrition_grade_fr = item["nutrition_grade_fr"]
                    prod.nutrition_score_fr_100g = \
                        int(item["nutriments"]["nutrition-score-fr_100g"])
                    prod.url = item["url"]
                    # add the product to the database, if necessary
                    prod.add_product_to_db(connection)
                    # update the database (table ProductCategory), if necessary
                    prod.add_product_category_to_db(categ_name, connection)
                    # if applicable, link the stores and the product
                    try:
                        shop_names = [
                            shop.strip() for shop in item["stores"].split(",")
                        ]
                    except KeyError: # no store mentioned here
                        # skip this step
                        continue
                    else:
                        for shop_name in shop_names:
                            # initiate a new instance of store
                            shop = Store(shop_name)
                            # add the store to the database, if necessary
                            shop.add_store_to_db(connection)
                            # update the database (table ProductStore)
                            prod.add_product_store_to_db(shop_name, connection)
    # close the connection to the database
    connection.close()


if __name__ == "__main__":
    main()
