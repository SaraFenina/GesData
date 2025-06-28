"""
    Auteur : Sara Fenina
    Créé le 16/04/2025
    PARTIE 2 : Semaine 2
    Tests de la fonction :
                           nombre_occurrences_niveau
"""


from SF_02_listes_type import *

from SF_02_listes_type import *

# TEST 1
print("---------------------------------------------------------------------------")
print("TEST 1 : Cas général (valeur présente)")
test = [
    Formation("Science", "Maths", 5),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 15),
    Formation("Science", "Informatique", 20),
    Formation("Lettres", "Philosophie", 25)]
valeur = 15

print("Indice où se trouve 15 :", nombre_occurrences_niveau(test, valeur)) # Il est attendu d'avoir 1

# TEST 2
print("---------------------------------------------------------------------------")
print("TEST 2 : Valeur absente")
valeur = 13

print("Indice où se trouve 13 :", nombre_occurrences_niveau(test, valeur)) #0

# TEST 3
print("---------------------------------------------------------------------------")
print("TEST 3 : Un seul élément dans la liste (valeur présente)")
test = [Formation("Science", "Maths", 42)]
valeur = 42

print("Indice où se trouve 42 :", nombre_occurrences_niveau(test, valeur)) #1

# TEST 4
print("---------------------------------------------------------------------------")
print("TEST 4 : Un seul élément dans la liste (valeur absente)")
valeur = 10
print("Indice où se trouve 10 :", nombre_occurrences_niveau(test, valeur)) #0

# TEST 5
print("---------------------------------------------------------------------------")
print("TEST 5 : Liste vide")
test = []
valeur = 10

print("Indice où se trouve 10 :", nombre_occurrences_niveau(test, valeur)) #0

# TEST 6
print("---------------------------------------------------------------------------")
print("TEST 6 : Plusieurs occurrences de la même valeur dans une liste de taille impaire")
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 10)]
valeur = 10

print("Indice (quelconque) d’un 10 trouvé :", nombre_occurrences_niveau(test, valeur))  #5

# TEST 7
print("---------------------------------------------------------------------------")
print("TEST 7 : Plusieurs occurrences de la même valeur dans une liste de taille paire")
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 10),
    Formation("lettres", "Chimie", 10)]
valeur = 10

print("Indice (quelconque) d’un 10 trouvé :", nombre_occurrences_niveau(test, valeur))  #6


#TEST 8 : liste très grande
print("---------------------------------------------------------------------------")
print("TEST 8 :")
print("Cas d'une liste très grande (10000 éléments)\n")

test = []
for i in range(10000):
    test.append(Formation("Science", "info", 10))  # niveaux 10 se repete 10000 fois 

print("Indice (quelconque) d’un 10 trouvé :", nombre_occurrences_niveau(test, valeur)) #10000

