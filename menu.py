#! /usr/bin/env python3
# coding: utf-8

"""This module contains the 'Menu' class and a display function."""


from category import Category
from product import Product
from savedproduct import SavedProduct


class Menu:
    """This class is used to represent the menus in the program."""

    def __init__(self):
        """This special method is the class constructor."""
        self.status = ["main_menu"] # type is list (of str)
        self.choices = {} # type is dict (values type is int)

    def display_categ(self, connection):
        """This method is responsible for displaying the list of categories."""
        print("\nDans quelle catégorie souhaitez-vous remplacer un aliment ?")
        # initiate a cursor
        cursor = connection.cursor()
        # get each category_id and category_name
        cursor.execute("""SELECT Category.id, Category.name FROM Category""")
        categ_rows = cursor.fetchall()
        # display possible choices
        proposals = [f"{row[0]} - {row[1]}" for row in categ_rows] + \
                    ["0 - Revenir au menu principal"]
        print("")
        for prop in proposals:
            print(prop)
        answer = ""
        # check answer validity
        while answer not in [num[0] for num in proposals]:
            answer = input("\nVotre choix : ")
        if answer == "0":
            # go back to the previous menu
            self.previous()
        else:
            # register the user choice
            self.choices["categ"] = int(answer)
            # go to the next menu
            self.next("prod_list")

    def display_main(self):
        """This method is responsible for displaying the main menu."""
        # display possible choices
        proposals = ["1 - Quel aliment souhaitez-vous remplacer ? ",
                     "2 - Retrouver mes aliments substitués",
                     "0 - Quitter le programme"
                    ]
        print("Menu principal :")
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

    def display_my_subs(self, connection):
        """This method is responsible for displaying
        the registered substitutes.
        """
        print("\nVoici la liste des substituts enregistrés :\n")
        # initiate a cursor
        cursor = connection.cursor()
        # get all data from SavedProduct table
        cursor.execute("""SELECT sp.product_id,
                                 sp.substitute_id,
                                 DATE_FORMAT(sp.save_date, "%d/%m/%Y")
                          FROM SavedProduct AS sp""")
        saved_rows = cursor.fetchall() # type is list of tuples
        # display all extended records in SavedProduct table
        # (with data from Product table)
        for tup in saved_rows:
            # collect data from Product table for the product to be substituted
            cursor.execute("""SELECT p.id,
                                     p.code,
                                     p.product_name
                              FROM Product AS p
                              WHERE p.id = %s""", (tup[0], ))
            prod_row = cursor.fetchall() # list of 1 tuple
            # collect data from Product table for the registered substitute
            cursor.execute("""SELECT p.id,
                                     p.code,
                                     p.product_name
                              FROM Product AS p
                              WHERE p.id = %s""", (tup[1], ))
            sub_row = cursor.fetchall() # list of 1 tuple
            print(f"Enregistré le {tup[2]} :")
            print(f"({prod_row[0][1]}) {prod_row[0][2]}")
            print("Remplacé par")
            print(f"({sub_row[0][1]}) {sub_row[0][2]}\n")
        input("Appuyez sur Entrée pour continuer...")
        # go back to the main menu
        self.status = ["main_menu"]

    def display_prod(self, connection):
        """This method is responsible for displaying the list of products."""
        print("\nQuel aliment souhaitez-vous remplacer ?")
        categ_id = self.choices["categ"]
        prod_id = 0
        # initiate a cursor
        cursor = connection.cursor()
        # get each product_id, product_code and category_name
        cursor.execute("""SELECT p.id, p.code, p.product_name
                          FROM Product AS p
                          JOIN ProductCategory AS pc
                          ON p.id = pc.product_id
                          JOIN Category AS c
                          ON pc.category_id = c.id
                          WHERE c.id = %s""", (categ_id, ))
        prod_rows = cursor.fetchall() # list of tuples (id, code, product_name)
        prod_rows_list = [list(tup) for tup in prod_rows] # list of lists
        count = len(prod_rows)
        pages_nbr = ((count // 9) + 1) if count % 9 else (count // 9)
        # start at page #1
        landmark = 1
        proposals = display_nine_prod(landmark, prod_rows_list, count)
        # check answer validity
        answer = input("Votre choix : ")
        while answer not in [num[0] for num in proposals]:
            if answer == "<<":
                landmark = 1
            elif answer == "<":
                landmark = max(1, landmark - 1)
            elif answer == ">":
                landmark = min(pages_nbr, landmark + 1)
            elif answer == ">>":
                landmark = pages_nbr
            proposals = display_nine_prod(landmark, prod_rows_list, count)
            answer = input("Votre choix : ")
        if answer == "0":
            # go back to the previous menu
            self.previous()
        else:
            # retrieve the prod_id
            try:
                prod_id = prod_rows[(landmark - 1) * 9 + int(answer) - 1][0]
            except TypeError:
                raise ValueError(answer)
            self.next("suggested_sub")
        return (prod_id, categ_id)

    def display_suggested_sub(self, connection, prod_id, categ_id):
        """This method is responsible for displaying
        the suggested substitute."""
        # initiate a cursor
        cursor = connection.cursor()
        # get product code, name, nutrition grade and nutrition scores
        cursor.execute("""SELECT p.code, p.product_name,
                                 p.nutrition_grade_fr,
                                 p.nutrition_score_fr_100g
                          FROM Product AS p
                          WHERE p.id = %s""", (prod_id, ))
        prod_rows = cursor.fetchall()
        if not prod_rows:
            raise ValueError(prod_id)
        else:
            prod = prod_rows[0]
            print("\nAfin de remplacer le produit")
            print(f"({prod[0]}) - {prod[1]}")
            print(f"dont le nutri-score est {prod[2].upper()},")
            # get category name from category id
            cursor.execute("""SELECT Category.name
                              FROM Category
                              WHERE Category.id = %s""", (categ_id, ))
            categ_row = cursor.fetchall()
            if categ_row:
                categ = Category(categ_row[0][0])
            else:
                raise ValueError(categ_id)
            # get one best product in category
            best = categ.best_prod(connection) # type is tuple
            # print the result
            print("nous vous proposons le produit suivant :")
            print(f"({best[2]}) - {best[3]}")
            print(f"dont le nutri-score est {best[4].upper()}.")
            print(f"Voici le lien d'une description du produit :\n{best[6]}")
            # get the possible store(s) where to buy this suggested product
            cursor.execute("""SELECT p.id,
                                     s.name
                              FROM Product AS p
                              JOIN ProductStore AS ps
                              ON ps.product_id = p.id
                              JOIN Store AS s
                              ON ps.store_id = s.id
                              WHERE p.id = %s""", (best[1], ))
            store_rows = cursor.fetchall() # type is list of tuples
            # there has to be at least one row
            if len(store_rows) != 1 or store_rows[0][1] != "":
                print(f"Vous pouvez le trouver dans ce(s) magasin(s) :")
                for tup in store_rows:
                    print(tup[1])
            answer = ""
            # check answer validity
            while answer not in ("oui", "non"):
                print("\nSouhaitez-vous enregistrer ce substitut ?")
                answer = input("oui / non : ")
                answer = answer.lower()
            if answer == "oui":
                saved = SavedProduct(prod_id, best[1])
                saved.add_saved_prod_to_db(connection)
            elif answer == "non":
                print("\nLe substitut n'a pas été enregistré.\n")
            else:
                raise ValueError(answer)
            # go back to the main menu
            self.status = ["main_menu"]

    def next(self, menu_str):
        """This method is responsible for moving forward to the next menu."""
        self.status.append(menu_str)

    def previous(self):
        """This method is responsible for going back to the previous menu,
        or quit the program if the user is on the main menu.
        """
        self.status.pop()

    def quit(self):
        """This method is responsible for exiting from the main menu."""
        self.status = []


def display_nine_prod(landmark, prod_rows_list, count):
    """This function, called by the method display_prod()
    is responsible for displaying a batch of nine products.
    """
    minus = (landmark - 1) * 9 # smallest index on each page
    # adapt the id's per category (start=1, increment=+1)
    for num in range(1, count + 1):
        prod_rows_list[num - 1][0] = num
    # display possible choices
    proposals = [f"{prod_row[0] % 9 if (prod_row[0] % 9) else 9}"
                 + f"- ({prod_row[1]}) {prod_row[2]}"\
                 for prod_row in prod_rows_list[minus:minus + 9]
                ] + ["0 - Revenir au menu précédent (catégories)"]
    print("")
    for prop in proposals:
        print(prop)
    print(f"\nPage courante : {landmark}")
    print("'<<' : première page ; '<' : page précédente ; ",
        "'>' : page suivante ; '>>' : dernière page\n")
    return proposals
