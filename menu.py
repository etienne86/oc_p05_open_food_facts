#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Menu' class."""


from category import Category
from product import Product


class Menu:
    """This class is used to represent the menus used in the program."""

    # # dict of possible menus
    # MENUS = {
    #          # "main_menu": ["1 - Quel aliment souhaitez-vous remplacer ? ",
    #          #               "2 - Retrouver mes aliments substitués"],
    #          # "categ_list": [f"{count} - " + categ_str for count, categ_str
    #          #                in enumerate(Category.CATEGORIES_LIST, 1)] +
    #          #               ["0 - Revenir au menu principal"],
    #          "prod_list": #pass pass,           
    #          "suggested_sub": #pass pass
    #          "my_subs": ["s - Supprimer un aliment enregistré"]
    #                     ["0 - Revenir au menu principal"],
    #          "sub_to_del" : #pass pass, 
    #         }

    def __init__(self):
        """This special method is the class constructor."""
        self.status = ["main_menu"] # type is list (of str)
        self.choices = {} # type is dict (values type is int)

    # def answers(self):
    #     """This method is responsible for returning the accepted answers,
    #     depending on the current menu.
    #     """
    #     pass #pass

    def display_main(self):
        """This method is responsible for displaying the main menu."""
        proposals = ["1 - Quel aliment souhaitez-vous remplacer ? ",
                     "2 - Retrouver mes aliments substitués",
                     "0 - Quitter le programme"
                    ]
        print("")
        for prop in proposals:
            print(prop)
        answer = ""
        # check answer validity
        while answer not in [num[0] for num in proposals]:
            answer = input("\nVotre choix : ")
        # go to the next menu
        if answer == "0":
            self.previous() # quit the program
        elif answer == "1":
            self.next("categ_list")
        elif answer == "2":
            self.next("my_subs")
        else:
            raise ValueError(answer)

    def display_categ(self, connection):
        """This method is responsible for displaying the list of categories."""
        # initiate a cursor
        cursor = connection.cursor()
        # get each category_id and category_name
        cursor.execute("""SELECT Category.id, Category.name FROM Category;""")
        categ_rows = cursor.fetchall()
        proposals = [f"{row[0]} - {row[1]}" for row in categ_rows] + \
                    ["0 - Revenir au menu principal"]
        print("")
        for prop in proposals:
            print(prop)
        answer = ""
        # check answer validity
        while answer not in [num[0] for num in proposals]:
            answer = input("\nDans quelle catégorie souhaitez-vous " + \
                "remplacer un aliment ? ")
        if answer == "0":
            # back to the previous menu
            self.previous()
        else:
            # register the user choice
            self.choices["categ"] = int(answer)
            # go to the next menu
            self.next("prod_list")

    def display_my_subs(self):
        """This method is responsible for displaying
        the registered substitutes.
        """
        pass #pass

    def display_prod(self, connection):
        """This method is responsible for displaying the list of products."""
        categ_id = self.choices["categ"]
        # initiate a cursor
        cursor = connection.cursor()
        # get each category_id and category_name
        cursor.execute("""SELECT Product.id, Product.product_name
                          FROM Product
                          JOIN ProductCategory
                          ON Product.id = ProductCategory.product_id
                          JOIN Category
                          ON ProductCategory.category_id = Category.id
                          WHERE Category.id = %s;""", (categ_id, ))
        prod_rows = cursor.fetchall() # list of tuples (id, product_name)
        prod_rows_list = [list(tup) for tup in prod_rows] # list of lists
        prod_rows_modif = prod_rows # TEMPORARY LINE
        # # adapt the id's per category (start=1, increment=+1)
        # prod_rows_modif = [(num, prod_rows_list[item][1]) \
        #                    for num, item in enumerate(prod_rows_list, 1)
        #                   ]
        proposals = [f"{prod_row[0]} - {prod_row[1]}" \
                     for prod_row in prod_rows_modif[0:10]
                    ] + ["0 - Revenir au menu précédent (catégories)"]
        print("")
        for prop in proposals:
            print(prop)
        answer = ""
        # check answer validity
        while answer not in [num[0] for num in proposals]:
            answer = input("\nQuel aliment souhaitez-vous remplacer ? ")
        while answer in (">", "<"):
            if answer == ">":
                pass
            elif answer == "<":
                pass
            else:
                raise ValueError(answer)
        if answer == "0":
            # back to the previous menu
            self.previous()
        else:
            self.next("suggested_sub")

    def display_sub_to_del(self):
        """This method is responsible for displaying
        the substitute to be deleted."""
        pass #pass

    def display_suggested_sub(self):
        """This method is responsible for displaying
        the suggested substitute."""
        print("\nin progress...")
        self.status = []

    def next(self, menu_str):
        """This method is responsible for moving forward to the next menu."""
        self.status.append(menu_str)

    def previous(self):
        """This method is responsible for going back to the previous menu,
        or quit the program if the user is on the main menu.
        """
        self.status.pop()

    def prod_id(self, big_id):
        """This method is responsible for transforming
        a "big id" (between 1 and 1000) to an id adapted
        to the 'products' menu (between 1 and 9).
        This adapted id is the first element in the returned tuple.
        The second element is a landmark to browse pages of products.
        """
        if big_id % 9:
            return (big_id % 9, big_id // 9)
        else:
            return (9, big_id // 9)

    def quit(self):
        """This method is responsible for exiting from the main menu."""
        self.status = []








