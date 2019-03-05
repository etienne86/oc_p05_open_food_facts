#! /usr/bin/env python3
# coding: utf-8

"""
Please execute this module to fill the products from OpenFoodFacts
into the database pur_beurre_05.
"""


import re

import mysql.connector
import requests

from category import Category
from product import Product
from store import Store


def main():
    """doctrinsg"""

    # connect to the database pur_beurre_05
    connexion = mysql.connector.connect(host="localhost",
                                        user="pur_guest",
                                        database="pur_beurre_05"
                                        )

    # iterate on each category pre-selected
    for categ_name in Category.CATEGORIES_LIST:
    #for categ_name in ["desserts"]:
        categ = Category(categ_name)
        # add the category to the database
        categ.add_category_to_db(connexion)
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
                        and ("nutrition_grade_fr" in item.keys()) \
                        and ("nutrition-score-fr_100g" in item["nutriments"].keys()) \
                        and ("nutrition-score-uk_100g" in item["nutriments"].keys()):
                    # set the product attributes
                    prod.code = int(item["code"])
                    prod.product_name = item["product_name"]
                    prod.nutrition_grade_fr = item["nutrition_grade_fr"]
                    prod.nutrition_score_fr_100g = \
                            int(item["nutriments"]["nutrition-score-fr_100g"])
                    prod.nutrition_score_uk_100g = \
                            int(item["nutriments"]["nutrition-score-uk_100g"])
                    prod.url = item["url"]
                    print("produit = ", prod.code)
                    # add the product to the database, if necessary
                    prod.add_product_to_db(connexion)
                    # update the database (table ProductCategory), if necessary
                    prod.add_product_category_to_db(categ_name, connexion)
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
                            shop.add_store_to_db(connexion)
                            # update the database (table ProductStore)
                            prod.add_product_store_to_db(shop_name, connexion)

    # close the connexion to the database
    connexion.close()


if __name__ == "__main__":
    main()
