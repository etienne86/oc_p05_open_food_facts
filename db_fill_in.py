#! /usr/bin/env python3
# coding: utf-8

"""
Please execute this module to fill the products from OpenFoodFacts
into the database pur_beurre_05.
"""


import mysql.connector
import requests

from category import Category
from product import Product
from product_store import ProductStore
from store import Store


def add_store_to_db(new_store):
    """docstring"""
    pass pass


def add_product_to_database(prod):
    """docstring"""
    pass pass


def sub_main():
    for categ in CATEGORIES_LIST:
        desserts_20 = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=desserts&page_size=20&json=1")
        if desserts_20.status_code == 200 and desserts_20.json()["count"]:
            api_return = desserts_20.json() # type is dict
            products_list = api_return["products"] # type is list of dict
            # iterate on each product
            for item in products_list:
                # initiate a new instance of product
                prod = Product()
                # filter on:
                # - products containing "France" in the list of countries
                # - products with 'nutrition_grade_fr' and 'code' completed
                regexp = "(.*)[Ff]rance(.*)"
                if re.match(regexp, item["countries"]) is not None \
                        and "nutrition_grade_fr" in item.keys() \
                        and "code" in item.keys():
                    # set the product attributes
                    prod.nutrition_grade_fr = item["nutrition_grade_fr"]
                    prod.code = item["code"]
                    prod.product_name = item["product_name"]
                    prod.nutrition_score_fr_100g = item["nutrition_score_fr_100g"]
                    prod.nutrition_score_uk_100g = item["nutrition_score_uk_100g"]
                    prod.url = item["url"]

                    # if applicable, link the stores and the product
                    try:
                        stores_list = [shop.strip() for shop in item["stores"].split(",")]
                    except KeyError: # no store mentioned here
                        # skip this step
                        continue
                    else:
                        for shop in stores_list:
                            shop.add_store_to_db() # add to the database, if necessary
                            prod_shop = ProductStore(prod.code, shop)
                            prod_shop.sql_insert() # update the database
                # add the product to the database
                prod.add_product_to_db()



def main():
    """docstring"""
    
    # connect to the database pur_beurre_05
    # connexion = mysql.connector.connect(host="localhost",
    #                                     user="pur_guest",
    #                                     database="pur_beurre_05"
    #                                     )
    connexion = mysql.connector.connect(host="localhost",
                                        user="pur_guest",
                                        database="pur_beurre_05"
                                        )

    # initiate a cursor
    cursor = connexion.cursor()

    # insert data
    for prod_dict in PRODUCT_EXAMPLES:
        for key in prod_dict:
            if key in list:
                pass
            elif key == "store":
                pass

        cursor.execute("""INSERT INTO Product (product_name,
                                               nutrition_score_fr_100g,
                                               nutrition_grade_fr,
                                               nutrition_score_uk_100g,
                                               url)
                          VALUES(%(product_name)s,
                                 %(nutrition_score_fr_100g)s,
                                 %(nutrition_grade_fr)s,
                                 %(nutrition_score_uk_100g)s,
                                 %(url)s)""", prod_dict)

    # commit the changes
    connexion.commit()

    # close the connexion to the database
    connexion.close()


if __name__ == "__main__":
    main()
