"""
    Auteur : Sara Fenina
    Crée le 21/03/2025
    PARTIE 1 :Semaine 3
    Test des fonction SF_fonction_en_plus qui permettent a SF_10_analyseur de bien fonctionner :
             Fonction
                         verif_critere
                      
"""

from SF_fonction_en_plus import *

# TEST 
print("---------------------------------------------------------------------------")
print("TEST : Vérification du critère alphabétique")
print("On teste la fonction verif_critere avec différentes entrées.\n")
print("Test 1")
print("Entrée : 'Science' ->", verif_critere("Science"))  # Il est attendu d'avoir True

print("\nTest 2")
print("Entrée : '123' ->", verif_critere("123"))   # False

print("\nTest 3")
print("Entrée : 'économie' ->", verif_critere("économie"))  # True

print("\nTest 4")
print("Entrée : 'Bio-logie' ->", verif_critere("Bio-logie")) # True



