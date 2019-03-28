# oc\_p05\_open\_food\_facts

Ceci est une notice d'installation et d'utilisation du programme en français, reprenant deux rubriques du fichier README.md.

## Comment installer le programme

Pre-requis:
* MySQL doit être installer sur votre ordinateur, avec un utilisateur 'root' déjà paramétré en tant qu'administrateur.

Veuillez exécuter ces lignes de code SQL dans le terminal MySQL, identifié en tant que 'root' :

    -- create a user
    CREATE USER 'pur_guest'@'localhost'; -- password is useless
    -- create the database pur_beurre_05
    CREATE DATABASE pur_beurre_05 CHARACTER SET 'utf8mb4';
    USE pur_beurre_05;
    -- assign rights to this user on the database
    GRANT ALL PRIVILEGES ON pur_beurre_05.* TO 'pur_guest'@'localhost';

Veuillez suivre les étapes suivantes :
* Ouvrez le terminal (Linux and MacOS) ou Windows PowerShell (Windows).
* Placez-vous sur le chemin où vous souhaitez installer le programme :
    * par exemple `cd this/is/my/path` sur Linux et MacOS
    * par exemple `cd C:\this\is\my\path` sur Windows
* Saisissez la commande suivante pour rapatrier le répertoire depuis GitHub: `git clone https://github.com/etienne86/oc_p05_open_food_facts.git`.
* Placez-vous vers ce nouveau répertoire dans votre console.
* Saisissez la commande suivante pour installer virtualenv (s'il n'est pas déjà installé): `pip install virtualenv`.
* Saisissez la commande suivante pour installer l'environnement virtuel : `virtualenv env`.
* Saisissez la commande suivante pour activer l'environnement virtuel :
    * `source env/bin/activate` sur Linux et MacOS
    * `./env/scripts/activate.ps1` sur Windows
* Saisissez la commande suivante pour installer les dépendances : `pip install -r requirements.txt`
* Saisissez la commande suivante pour initialiser et remplir la base de données : `python db_init.py`
* Saisissez la commande suivante pour désactiver l'environnement virtuel : `deactivate` 

Félicitations ! Vous avez terminé l'installation.


## Comment utiliser le programme

Veuillez suivre les étapes suivantes :
* Ouvrez le terminal (Linux and MacOS) ou Windows PowerShell (Windows).
* Sur la console, placez-vous sur le répertoire d'installation du programme.
* Saisissez la commande suivante pour activer l'environnement virtuel :
    * `source env/bin/activate` sur Linux et MacOS
    * `./env/scripts/activate.ps1` sur Windows
* Saisissez la commande suivante pour  exécuter le programme principal : `python substitute.py`

Ensuite, merci de suivre le guide indiqué dans les *user stories* ci-dessous : commencez avec US01.

### US01 : je veux voir le menu principal pour saisir mon choix

Précédent : soit j'ai juste démarré le programme, soit j'ai décidé de revenir au menu principal (US07, US08, US09 or US10).

Le menu principal affiche trois choix possibles :
1. Querl aliment souhaitez-vous remplacer ?
2. Retrouver mes aliments substitués
0. Quitter le programme

Suivant : je saisis soit `1` (cf. US02), soit `2` (cf. US09), soit `0` (cf. US11).

### US02 : je veux saisir `1` dans le menu principal pour afficher les catégories d'aliments

Précédent : j'étais dans le menu principal (US01)

Je saisis `1`, et je valide avec "Entrée".

Suivant : US03

### US03 : je veux saisir un chiffre pour sélectionner une catégorie d'aliment et afficher les aliments de cette catégorie

Précédent : US02

Le menu affiche une liste de neuf catégories. Je saisis un chiffre entre 1 et 9 pour sélectionner la catégorie souhaitée, et je valide avec "Entrée".

Note : je peux également saisir `0` pour revenir au menu précédent (menu principal) (cf. US10).

Suivant : US04

### US04 : je veux saisir un chiffre pour sélectionner un aliment à remplacer

Précédent : US03

Le menu affiche une liste de neuf aliments. Je saisis un chiffre entre 1 et 9 pour sélectionner l'aliment souhaité, et je valide avec "Entrée".

Note — je peux également :
* naviguer de page en page pour voir tous les aliments (cf. US 05)
* retourner au menu principal si je saisis `0` (cf. US10)

Suivant : US06

### US05 : je veux naviguer de page en page parmi les aliments d'une catégorie

Précédent : US04

Je peux :
* saisir `<<` pour voir les produits de la première page, et valider avec "Entrée"
* saisir `<` pour voir les produits de la page précédente, et valider avec "Entrée"
* saisir `>` pour voir les produits de la page suivante, et valider avec "Entrée"
* saisir `>>` pour voir les produits de la dernière page, et valider avec "Entrée"

Suivant : US04

### US06 : je veux voir une proposition d'aliment de substitution pour pouvoir le sauvegarder si je le souhaite

Précédent : US04

Le programme affiche et propose un aliment de substitution à mon produit sélectionné. Le menu affiche deux choix possibles :
* `oui` si je veux sauvegarder le substitut proposé
* `non` si je ne veux pas sauvegarder le substitut proposé

Suivant : je saisis soit `oui` (cf. US07) soit `non` (cf. US08)

### US07 : je veux saisir `oui` pour enregistrer le substitut proposé dans la base de données

Précédent : US06

Je saisis `oui`, et je valide avec "Entrée". L'aliment initial et le substitut sont sauvegardés. Le programme revient au menu principal.

Suivant : US01

### US08 : je veux saisir `non` pour ne pas enregistrer le substitut proposé

Précédent : US06

Je saisis `non`, et je valide avec "Entrée". Rien n'est enregistré. Le programme revient au menu principal.

Suivant : US01

### US09 : je veux saisir `2` dans le menu principal pour retrouver mes aliments substitués

Précédent : j'étais dans le menu principal (US01)

Je saisis `2`, et je valide avec "Entrée". Le programme affiche la liste de mes aliments enregistrés (aliments initiaux et de substitution), avec la date d'enregistrement. Je valide avec "Entrée" pour revenir au menu principal.

Suivant : US01

### US10 : je veux saisir `0` dans une rubrique pour revenir au menu précédent

Précédent : US03 ou US04

Je saisis `0`, et je valide avec "Entrée". Le programme affiche le menu précédent.

Suivant : US01 (si le précédent était US03) ou US03 (si le précédent était US04)

### US11 : je veux saisir `0` dans le menu principal pour quitter le programme

Précédent : j'étais dans le menu principal (US01)

Je saisis `0`, et je valide avec "Entrée".
Le programme se termine et se ferme.
