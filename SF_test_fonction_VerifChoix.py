"""
    Auteur : Sara Fenina
    Crée le 21/03/2025
    PARTIE 1 :Semaine 3
    Test des fonction SF_fonction_en_plus qui permettent a SF_10_analyseur de bien fonctionner :
             Fonction 
                      verif_choix
"""

from SF_fonction_en_plus import *

# TEST 
print("---------------------------------------------------------------------------")
print("TEST  : Vérification du choix utilisateur")
print("On teste la fonction verif_choix avec différentes entrées.\n")
print("Test 1")
print("Entrée : '1', Taille liste : 5 ->", verif_choix("1", 5))  # Il est attendu d'avoir True

print("\nTest 2")
print("Entrée : '5', Taille liste : 5 ->", verif_choix("5", 5))  # True

print("\nTest 3")
print("Entrée : '0', Taille liste : 5 ->", verif_choix("0", 5))  # False

print("\nTest 4")
print("Entrée : '6', Taille liste : 5 ->", verif_choix("6", 5))  # False

