# oc\_p05\_open\_food\_facts

Project #05 in OC Python course

Author: etienne86

## Purpose

This program suggests alternative healthy food to consumers, based on OpenFoodFacts database.

## Short description

The user select a food in the terminal, then the program suggest an alternative healthy food in return. The user can save this substitute, or not. Saved substitutes can be found back later on.

## How to install the program

Pre-requisite: mysql has to be installed on your computer, with a 'root' user already set up.

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
* Enter the following command to install the dependancies: `pip install -r requirements.txt`
* Enter the following command to get the database initialized and filled in: `python db_init.py`
* Enter the following command to deactivate the virtual environment:
    * `source env/bin/deactivate` for Linux and MacOS
    * `./env/scripts/activate.ps1` for Windows
    
Congratulations! You have completed the program installation.

## How to read the program (for programmers)

### Program architecture

TO DO

### Agile dashboard

[Link to Trello dashboard](https://trello.com/b/Q6r47F1d/e-barbier-oc-da-py-open-food-facts)

## How to use the program (for users), user stories

Please follow the next steps:
* Open your terminal (Linux and MacOS) or Windows PowerShell (Windows).
* On your terminal, move to the directory where the program is installed.
* Enter the following command to activate the virtual environment:
    * `source env/bin/activate` for Linux and MacOS
    * `./env/scripts/activate.ps1` for Windows
* Enter the following command to execute the main program: `python substitute.py`

Then, please follow the guide indicated in the user stories below: start with US01.

### US01: I want to see the main menu to enter my choice

Previous: either I have just started the program, or I decided to go back to the main menu (US07, US08, US09 or US10).

The main menu displays three choices:
1. Which foodstuff do I want to replace?
2. My saved foodstuffs
0. Quit the program

Next: I enter either `1` (cf. US02), or `2` (cf. US09), or `0` (cf. US11).

### US02: I want to enter `1` in the main menu to display the food categories

Previous: I was on the main menu (US01).

I enter `1`, and valid with "Enter".

Next: US03

### US03: I want to enter a number to select a food category and display its foodstuffs

Previous: US02

The menu displays a list of nine food categories. I enter a number between 1 and 9 to select the chosen food category, and valid with "Enter".

Note: I can also enter `0` to go back to the previous menu (main menu) (cf. US10).

Next: US04

### US04: I want to enter a number to select a foodstuff to replace

Previous: US03

The menu displays a list of nine foodstuffs. I enter a number between 1 and 9 to select the chosen foodstuff to replace, and valid with "Enter".

Note — I can also:
* browse pages to see all foodstuffs (cf. US 05)
* go back to the main menu if I enter `0` (cf. US10)

Next: US06

### US05: I want to browse pages to see all foodstuffs in a category

Previous: US04

I can:
* enter `<<` to see products on first page, and valid with "Enter"
* enter `<` to see products on previous page, and valid with "Enter"
* enter `>` to see products on next page, and valid with "Enter"
* enter `>>` to see products on last page, and valid with "Enter"

Next: US04

### US06: I want to see a suggested substitute to my selected product

Previous: US04

The program displays and suggest a substitute foodstuff to my selected product. The main menu displays two choices:
* `oui` if I want to save the suggested substitute
* `non` if I do not want to save the suggested substitute

Next: I enter either `oui` (cf. US07) or `non` (cf. US08).

### US07: I want to enter `oui` to save the suggested substitute

Previous: US06

I enter `oui`, and valid with "Enter". The origin food and the substitute food are saved. The program goes back to the main menu.

Next: US01

### US08: I want to enter `non` not to save the suggested substitute

Previous: US06

I enter `non`, and valid with "Enter". Nothing is saved. The program goes back to the main menu.

Next: US01

### US09: I want to enter `2` in the main menu to display my saved foodstuffs

Previous: I was on the main menu (US01).

I enter `2`, and valid with "Enter". The program displays the list of my saved foodstuffs (origin food and substitute food), with the record date. I valid with "Enter" to go back to the main menu.

Next: US01

### US10: I want to enter `0` in somes menus to go back to the previous menu

Previous: US03 or US04

I enter `0`, and valid with "Enter". The program displays the previous menu.

Next: US01 (if previous was US03) or US03 (if previous was US04)

### US11: I want to enter `0` in the main menu to quit the program

Previous: US01

I enter `0`, and valid with "Enter".
The program ends and quits.
