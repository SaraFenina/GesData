"""
    Auteur : Sara Fenina
    Créé le 16/04/2025
    PARTIE 2 : Semaine 2
    Tests de la fonction :
                           recherche_petit_niveau
"""

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

print("Indice où se trouve 15 :", recherche_petit_niveau(test, valeur)) # Il est attendu d'avoir 2

# TEST 2
print("---------------------------------------------------------------------------")
print("TEST 2 : Valeur absente")
valeur = 13

print("Indice où se trouve 13 :", recherche_petit_niveau(test, valeur)) #-1

# TEST 3
print("---------------------------------------------------------------------------")
print("TEST 3 : Un seul élément dans la liste (valeur présente)")
test = [Formation("Science", "Maths", 42)]
valeur = 42

print("Indice où se trouve 42 :", recherche_petit_niveau(test, valeur)) #0

# TEST 4
print("---------------------------------------------------------------------------")
print("TEST 4 : Un seul élément dans la liste (valeur absente)")
valeur = 10
print("Indice où se trouve 10 :", recherche_petit_niveau(test, valeur)) #-1

# TEST 5
print("---------------------------------------------------------------------------")
print("TEST 5 : Liste vide")
test = []
valeur = 10

print("Indice où se trouve 10 :", recherche_petit_niveau(test, valeur)) #-1

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

print("Indice (quelconque) d’un 10 trouvé :", recherche_petit_niveau(test, valeur))  #0

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

print("Indice (quelconque) d’un 10 trouvé :", recherche_petit_niveau(test, valeur))  #0


#TEST 8

print("---------------------------------------------------------------------------")
print("TEST 8 : la valeur se trouve au debut (valeur présente)")
test = [
    Formation("Science", "Maths", 15),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 35),
    Formation("Science", "Informatique", 20),
    Formation("Lettres", "Philosophie", 25)]
valeur = 15

print("Indice d’un 10 trouvé :", recherche_petit_niveau(test, valeur)) #0


#TEST 9

print("---------------------------------------------------------------------------")
print("TEST 9 : la valeur se trouve a la fin (valeur présente)")
test = [
    Formation("Science", "Maths", 15),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 35),
    Formation("Science", "Informatique", 5),
    Formation("Lettres", "Philosophie", 5)]
valeur = 5

print("Indice d’un 10 trouvé :", recherche_petit_niveau(test, valeur)) #3


