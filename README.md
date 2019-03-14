# oc\_p05\_open\_food\_facts

Project #05 in OC Python course

Author: etienne86

## Purpose

Suggest alternative healthy food to consumers

## Short description

Users can enter any kind of food into the terminal, so that they can be suggested alternative healthy food in return

## How to install the program

Please follow the next steps:
* Open your terminal (Linux and MacOS) or Windows PowerShell (Windows).
* Setup the path where you want to install the program:
    * e.g. `cd this/is/my/path` for Linux and MacOS
    * e.g. `cd C:\this\is\my\path` for Windows
* Enter the following command to pull the repository from GitHub: `git clone https://github.com/etienne86/oc_p05_open_food_facts.git`.
* Move to this new directory on your terminal.
* Enter the following command to install virtualenv (if not already installed): `pip install virtualenv`.
* Enter the following command to install the virtual environment: `virtualenv env`.
* Enter the following command to activate the virtual environment:
    * `source env/bin/activate` for Linux and MacOS
    * `./env/scripts/activate.ps1` for Windows
* Enter the following command to get the database initialized: `python db_init.py`
* Enter the following command to get the database filled in: `python db_fill_in.py`
* Enter the following command to deactivate the virtual environment:
    * `source env/bin/deactivate` for Linux and MacOS
    * `./env/scripts/activate.ps1` for Windows
Congratulations! You have completed the program installation.

## How to read the program (technical specifications)

To do

## How to use the programm (functional specifications), user stories

Please follow the next steps:
* Open your terminal (Linux and MacOS) or Windows PowerShell (Windows).
* On your terminal, move to the directory where the program is installed.
* Enter the following command to activate the virtual environment:
    * `source env/bin/activate` for Linux and MacOS
    * `./env/scripts/activate.ps1` for Windows
* Enter the following command to execute the main program: `python substitute.py`

### US01: I want to see the main menu to enter my choice

Previous: either I have just started to use the program, or I decided to go back to the main menu (US11).
The main menu displays three choices:
1. Which foodstuff do I want to replace?
2. My registered foodstuffs
0. Quit the program
Next: I enter either `1` (cf. US02) or `2` (cf. US08).

### US02: I want to enter `1` in the main menu to display the food categories

Previous: I was on the main menu (US01).
I enter `1`, and valid with "Enter".
Note: I can also go back to the main menu if I enter `0` (cf. US11).
Next: US03

### US03: I want to enter a number to select a food category and display its foodstuffs

Previous: US02.
The menu displays a list of nine food categories.
I enter a number between 1 and 9 to select the chosen food category, and valid with "Enter".
Note: I can also go back to the main menu if I enter `0` (cf. US11).
Next: US04

### US04: I want to enter a number to select a foodstuff to replace

Previous: US03.
The menu displays a list of nine foodstuffs.
I enter a number between 1 and 9 to select the chosen foodstuffs to replace, and valid with "Enter".
If possible, I can also enter either `>` to see next products or `<` to go back to previous products.
Note: I can also go back to the main menu if I enter `0` (cf. US11).
Next: US05

## Agile dashboard

[Link to Trello dashboard](https://trello.com/b/Q6r47F1d/e-barbier-oc-da-py-open-food-facts)
