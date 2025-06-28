"""
    Auteur : Sara Fenina
    Crée le 21/03/2025
    PARTIE 1 :Semaine 3
    Test des fonction SF_10_analyseur :
             Fonction 
                      affiche_statistiques
"""

from SF_fonction_en_plus import *



# TEST 1
print("---------------------------------------------------------------------------")
print("TEST 1 : Cas général 1")
print("On teste la fonction avec une liste de valeurs variées.\n")
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 95)]
affiche_statistiques(test)
#il est attendu d'avoir
"""Les modalités des niveaux de formation sont :  [10, 95]
Le nombre d'enregistrements est 5
Le niveau maximum des formations est :  95
Le niveau minimum des formations est :  10
La moyenne des niveau est  27.0
L'ecart type des niveau de formation est  34.0
La mediane des niveau de formation est  10"""







# TEST 2
print("---------------------------------------------------------------------------")
print("TEST 2 : Un seul élément")
print("On teste la fonction avec une liste contenant un seul élément.\n")
test = [Formation("Science", "Maths", 42)]
affiche_statistiques(test)
#
"""Ci-suit les statistiques des niveaux de formation du fichier choisi 
Les modalités des niveaux de formation sont :  [42]
Le nombre d'enregistrements est 1
Le niveau maximum des formations est :  42
Le niveau minimum des formations est :  42
La moyenne des niveau est  42.0
L'ecart type des niveau de formation est  0.0
La mediane des niveau de formation est  4"""






# TEST 3
print("---------------------------------------------------------------------------")
print("TEST 3 : Valeurs négatives")
print("On teste la fonction avec une liste contenant des valeurs négatives.\n")
test = [
    Formation("Science", "Maths", -3),
    Formation("Science", "Physique", -1),
    Formation("Science", "Chimie", -7),
    Formation("Science", "Informatique", -4),
    Formation("Lettres", "Philosophie", -5)]
affiche_statistiques(test)
#
"""Les modalités des niveaux de formation sont :  [-3, -1, -7, -4, -5]
Le nombre d'enregistrements est 5
Le niveau maximum des formations est :  -1
Le niveau minimum des formations est :  -7
La moyenne des niveau est  -4.0
L'ecart type des niveau de formation est  2.0
La mediane des niveau de formation est  -7"""





# TEST 4
print("---------------------------------------------------------------------------")
print("TEST 4 : Valeurs identiques")
print("On teste la fonction avec une liste où toutes les valeurs sont identiques.\n")
test=[
    Formation("Science", "Maths", 15),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 15),
    Formation("Science", "Informatique", 15),
    Formation("Lettres", "Philosophie", 15)]
affiche_statistiques(test)
#
"""Les modalités des niveaux de formation sont :  [15]
Le nombre d'enregistrements est 5
Le niveau maximum des formations est :  15
Le niveau minimum des formations est :  15
La moyenne des niveau est  15.0
L'ecart type des niveau de formation est  0.0
La mediane des niveau de formation est  15"""
