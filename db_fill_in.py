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
from store import Store


def add_store_to_db(new_store):
    """docstring"""
    pass pass


def add_product_to_database(new_product):
    """docstring"""
    pass pass


def sub_main():
    for categ in CATEGORIES_LIST:
        desserts_20 = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=desserts&page_size=20&json=1")
        if desserts_20.status_code == 200 and desserts_20.json()["count"]:
            api_return = desserts_20.json() # type is dict
            products_list = api_return["products"] # type is list of dict
            # iterate on each product
            for product_dict in products_list:
                # initiate a new instance of product
                new_product = Product()
                # filter on:
                # - products containing "France" in the list of countries
                # - products with 'nutrition_grade_fr' completed
                regexp = "(.*)[Ff]rance(.*)"
                if re.match(regexp, product_dict["countries"]) is not None
                        and "nutrition_grade_fr" in product_dict.keys():
                    # set the product attributes
                    new_product.nutrition_grade_fr = product_dict["nutrition_grade_fr"]
                    new_product.code = product_dict["code"]
                    new_product.product_name = product_dict["product_name"]
                    new_product.nutrition_score_fr_100g = product_dict["nutrition_score_fr_100g"]
                    new_product.nutrition_score_uk_100g = product_dict["nutrition_score_uk_100g"]
                    new_product.url = product_dict["url"]

                    # if applicable, link the stores and the product
                    try:
                        stores_list = [each_store.strip() for each_store in product_dict["stores"].split(",")]
                    except KeyError: # no store mentioned here
                        # skip this step
                        continue
                    else:
                        for item in stores_list:
                            if item in STORES_LIST: # store already initiated
                                .add_code(new_product.code)
                            else:
                                new_store = Store(item)
                                new_store.add_code(new_product.code)
                                # add the store to the database
                                add_store_to_db(new_store)

                    # add the product to the database
                    add_product_to_database(new_product)



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
