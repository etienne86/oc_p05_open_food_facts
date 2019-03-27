#! /usr/bin/env python3
# coding: utf-8

"""This module contains:
- the 'Menu' class
- a display function, outside of the 'Menu' class, but used by the class
"""


from texttable import Texttable

from category import Category
from savedproduct import SavedProduct


class Menu:
    """This class is used to represent the menus in the program."""

    def __init__(self):
        """This special method is the class constructor."""
        self.status = ["main_menu"] # type is list (of str)
        self.choices = {} # type is dict (type of values is int)

    def display_categ(self, connection):
        """This method is responsible for displaying the list of categories."""
        # display the menu title
        string = "\n" + 110 * "*" + "\n*" + 43 * " " + "CATEGORIES D'ALIMENTS" \
                 + 44 * " " + "*\n" + 110 * "*"
        print(string)
        print("\nDans quelle catégorie souhaitez-vous remplacer un aliment ?")
        # initiate a cursor
        cursor = connection.cursor()
        # get each category_id and category_name
        cursor.execute("""SELECT Category.id, Category.name FROM Category""")
        categ_rows = cursor.fetchall()
        # display the possible choices
        table1 = Texttable()
        prop_table1 = [["Raccourci clavier", "Catégorie"]]
        for row in categ_rows:
            prop_table1.append([row[0], row[1]])
        # define the cells alignment
        table1.set_cols_align(['c', 'l']) # center, left
        table1.set_cols_width([17, 86])
        # draw the table
        table1.add_rows(prop_table1)
        print(table1.draw())
        # print the end of the categories menu
        table2 = Texttable()
        prop_table2 = [
            ["Raccourci clavier", "Autre choix"],
            ["0", "Revenir au menu principal"]
        ]
        # define the cells alignment
        table2.set_cols_align(['c', 'l']) # center, left
        table2.set_cols_width([17, 86])
        # draw the table
        table2.add_rows(prop_table2)
        print(table2.draw())
        answer = ""
        # check the answer validity
        while answer not in (str(i) for i in range(len(categ_rows)+ 1)):
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
        # display the menu title
        string = "\n" + 110 * "*" + "\n*" + 47 * " " + "MENU PRINCIPAL" \
                 + 47 * " " + "*\n" + 110 * "*" + "\n"
        print(string)
        # display the possible choices
        table1 = Texttable()
        prop_table1 = [
            ["Raccourci clavier", "Rubrique"],
            ["1", "Quel aliment souhaitez-vous remplacer ?"],
            ["2", "Retrouver mes aliments substitués"]
        ]
        # define the cells alignment
        table1.set_cols_align(['c', 'l']) # center, left
        table1.set_cols_width([17, 86])
        # draw the table
        table1.add_rows(prop_table1)
        print(table1.draw())
        # print the end of the main menu
        table2 = Texttable()
        prop_table2 = [
            ["Raccourci clavier", "Autre choix"],
            ["0", "Quitter le programme"]
        ]
        # define the cells alignment
        table2.set_cols_align(['c', 'l']) # center, left
        table2.set_cols_width([17, 86])
        # draw the table
        table2.add_rows(prop_table2)
        print(table2.draw())
        answer = ""
        # check answer validity
        while answer not in ("0", "1", "2"):
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
        # display the menu title
        string = "\n" + 110 * "*" + "\n*" + 43 * " " + "SUBSTITUTS ENREGISTRES" \
                 + 43 * " " + "*\n" + 110 * "*" + "\n"
        print(string)
        # initiate a cursor
        cursor = connection.cursor()
        # get all data from SavedProduct table
        cursor.execute("""SELECT sp.product_id,
                                 sp.substitute_id,
                                 DATE_FORMAT(sp.save_date, "%d/%m/%Y")
                          FROM SavedProduct AS sp
                          ORDER BY sp.save_date ASC""")
        saved_rows = cursor.fetchall() # type is list of tuples
        # display all extended records in SavedProduct table
        # (with data from Product table)
        table = Texttable()
        table_list = [
            ["Date\nenregistrement",
             "Code produit\ninitial",
             "Produit initial",
             "Code produit\ndu substitut",
             "Produit de substitution"
            ]
        ]
        # define the cells alignment:
        # horizontal: center, right, left, right, left
        table.set_cols_align(['c', 'r', 'l', 'r', 'l'])
        # vertical: middle for all columns
        table.set_cols_valign(['m', 'm', 'm', 'm', 'm'])
        table.set_cols_width([14, 13, 27, 13, 27])
        # define the columns type: text, int, text, int, text
        table.set_cols_dtype(['t', 'i', 't', 'i', 't'])
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
            record = [
                tup[2],
                prod_row[0][1],
                prod_row[0][2],
                sub_row[0][1],
                sub_row[0][2]
            ]
            table_list.append(record)
        # draw the table
        table.add_rows(table_list)
        print(table.draw())
        input("Appuyez sur Entrée pour continuer...")
        # go back to the main menu
        self.status = ["main_menu"]

    def display_prod(self, connection):
        """This method is responsible for displaying the list of products."""
        # initiate a cursor
        cursor = connection.cursor()
        # get each category name
        cursor.execute("""SELECT c.name
                          FROM Category AS c
                          WHERE c.id = %s""", (self.choices["categ"], ))
        categ_row = cursor.fetchall() # list of one tuple (category_name, )
        # display the menu title
        num = (83 - len(categ_row[0][0])) // 2
        if len(categ_row[0][0]) % 2:
            string = "\n" + 110 * "*" + "\n*" + num * " " \
                     + "PRODUITS DE LA CATEGORIE " + f"{categ_row[0][0]}" \
                     + num * " " + "*\n" + 110 * "*"
        else:
            string = "\n" + 110 * "*" + "\n*" + num * " " \
                     + "PRODUITS DE LA CATEGORIE " + f"{categ_row[0][0]}" \
                     + (num + 1) * " " + "*\n" + 110 * "*"
        print(string)
        print("\nQuel produit souhaitez-vous remplacer ?")
        # get each product_id, product_code and product_name
        cursor.execute("""SELECT p.id, p.code, p.product_name
                          FROM Product AS p
                          JOIN ProductCategory AS pc
                          ON p.id = pc.product_id
                          JOIN Category AS c
                          ON pc.category_id = c.id
                          WHERE c.id = %s""", (self.choices["categ"], ))
        prod_rows = cursor.fetchall() # list of tuples (id, code, product_name)
        prod_rows_list = [list(tup) for tup in prod_rows] # list of lists
        count = len(prod_rows)
        pages_nbr = ((count // 9) + 1) if count % 9 else (count // 9)
        # start at page #1
        landmark = 1
        proposals = display_nine_prod(landmark, prod_rows_list, count)
        # check answer validity
        answer = input("Votre choix : ")
        while answer not in [prop[0] for prop in proposals]:
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
        prod_id = 0
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
        return (prod_id, self.choices["categ"])

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
        row = cursor.fetchall() # type is list of one tuple
        if not row:
            raise ValueError(prod_id)
        prod = row[0]
        print("\nAfin de remplacer le produit :")
        # 1. display the initial product
        table = Texttable()
        table_list = [
            ["Code produit", "Désignation", "Nutriscore"],
            [prod[0], prod[1], prod[2].upper()]
        ]
        # define the cells alignment
        table.set_cols_align(['r', 'l', 'c']) # right, left, center
        table.set_cols_valign(['m', 'm', 'm']) # middle, middle, middle
        table.set_cols_width([13, 77, 10])
        # define the columns type
        table.set_cols_dtype(['i', 't', 't']) # text, int, text
        # draw the table
        table.add_rows(table_list)
        print(table.draw())
        # get category name from category id
        cursor.execute("""SELECT Category.name
                          FROM Category
                          WHERE Category.id = %s""", (categ_id, ))
        row = cursor.fetchall() # type is list of one tuple
        if row:
            categ = Category(row[0][0])
        else:
            raise ValueError(categ_id)
        # get one best product in category
        best = categ.best_prod(connection) # type is tuple
        # print the result
        print("\nNous vous proposons le produit suivant :")
        # 2. display the substitute product
        table = Texttable()
        table_list = [
            ["Code produit", "Désignation", "Nutriscore"],
            [best[2], best[3], best[4].upper()]
        ]
        # define the cells alignment
        table.set_cols_align(['r', 'l', 'c']) # right, left, center
        table.set_cols_valign(['m', 'm', 'm']) # middle, middle, middle
        table.set_cols_width([13, 77, 10])
        # define the columns type
        table.set_cols_dtype(['i', 't', 't']) # text, int, text
        # draw the table
        table.add_rows(table_list)
        print(table.draw())
        print(f"\nVoici le lien d'une description du produit :\n{best[6]}")
        # get the possible store(s) where to buy this suggested product
        cursor.execute("""SELECT p.id,
                                 s.name
                          FROM Product AS p
                          JOIN ProductStore AS ps
                          ON ps.product_id = p.id
                          JOIN Store AS s
                          ON ps.store_id = s.id
                          WHERE p.id = %s""", (best[1], ))
        rows = cursor.fetchall() # type is list of tuples
        # there has to be at least one row
        if len(rows) != 1 or rows[0][1] != "":
            print(f"\nVous pouvez le trouver dans ce(s) magasin(s) :")
            for row in rows:
                print(row[1])
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
    """This function, called by the method display_prod(),
    is responsible for displaying:
    - a batch of nine products (or less if this is the last page)
    - the end of the products menu to browse pages
    """
    minus = (landmark - 1) * 9 # smallest index on each page
    # adapt the id's per category (start=1, increment=+1)
    for num in range(1, count + 1):
        prod_rows_list[num - 1][0] = num
    # possible choices
    proposals = [f"{prod_row[0] % 9 if (prod_row[0] % 9) else 9}"\
                 for prod_row in prod_rows_list[minus:minus + 9]
                ] + ["0"]
    # display the possible choices
    table1 = Texttable()
    prop_table1 = [["Raccourci clavier", "Code produit", "Désignation"]]
    for prod_row in prod_rows_list[minus:minus + 9]:
        item = f"{prod_row[0] % 9 if (prod_row[0] % 9) else 9}"
        prop_table1.append([item, f"{prod_row[1]}", f"{prod_row[2]}"])
    # define the cells alignment
    table1.set_cols_align(['c', 'r', 'l']) # center, right, left
    table1.set_cols_valign(['m', 'm', 'm']) # middle, middle, middle
    table1.set_cols_width([17, 13, 70])
    # define the columns type
    table1.set_cols_dtype(['t', 'i', 't']) # text, int, text
    # draw the table
    table1.add_rows(prop_table1)
    print(table1.draw())
    # print the end of menu
    table2 = Texttable()
    pages_nbr = ((count // 9) + 1) if count % 9 else (count // 9)
    prop_table2 = [
        ["Raccourci clavier",
         f"Autres choix (page courante : page {landmark} sur {pages_nbr})"
        ]
    ]
    prop_table2.append(["0", "Revenir au menu précédent (catégories)"])
    prop_table2.append(["<<", "Aller à la première page"])
    prop_table2.append(["<", "Aller à la page précédente"])
    prop_table2.append([">", "Aller à la page suivante"])
    prop_table2.append([">>", "Aller à la dernière page"])
    # define the cells alignment
    table2.set_cols_align(['c', 'l']) # center, left
    table2.set_cols_valign(['m', 'm']) # middle, middle
    table2.set_cols_width([17, 86])
    # define the columns type
    table2.set_cols_dtype(['t', 't']) # text, text
    # draw the table
    table2.add_rows(prop_table2)
    print(table2.draw())
    return proposals
