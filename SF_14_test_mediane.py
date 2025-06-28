"""
    Auteur : Sara Fenina
    Crée le 07/04/2025
    PARTIE 2 : Semaine 1
    Programme de test de la fonction mediane_niveau qui se trouve dans le fichier SF_02_listes_type
"""




from SF_02_listes_type import *

# Programme de test pour la fonction mediane_niveau

# TEST 1 : Liste vide
print("--------------------------------------------------")
print("TEST 1 : Liste vide")
test = []
print("Liste : ", test)
if len(test) == 0:
    print("Pas de médiane possible pour une liste vide.")
else:
    print("\nMédiane :", mediane_niveau(test)) # Il est attendu d'avoir Pas de médiane possible pour une liste vide.


# TEST 2 : Liste avec un seul élément
print("--------------------------------------------------")
print("TEST 2 : Liste avec un seul élément")
test = [Formation("Domaine", "Intitulé", 10)]
affiche_liste_Formation(test)
print("\nMédiane calculée :", mediane_niveau(test)) #10


# TEST 3 : Liste avec un nombre impair d'éléments
print("--------------------------------------------------")
print("TEST 3 : Liste impaire")
test = [
    Formation("A", "X", 2),
    Formation("B", "Y", 5),
    Formation("C", "Z", 8)
]
affiche_liste_Formation(test)
print("\nMédiane calculée :", mediane_niveau(test)) #5


# TEST 4 : Liste avec un nombre pair d'éléments
print("--------------------------------------------------")
print("TEST 4 : Liste paire")
test = [
    Formation("A", "X", 2),
    Formation("B", "Y", 4),
    Formation("C", "Z", 6),
    Formation("D", "W", 8)
]
affiche_liste_Formation(test)
print("\nMédiane calculée :", mediane_niveau(test)) #5.0


# TEST 5 : Liste plus grande (10 éléments)
print("--------------------------------------------------")
print("TEST 5 : Liste de taille 10")
test = [
    Formation("D", "X", 1),
    Formation("D", "X", 2),
    Formation("D", "X", 3),
    Formation("D", "X", 4),
    Formation("D", "X", 5),
    Formation("D", "X", 6),
    Formation("D", "X", 7),
    Formation("D", "X", 8),
    Formation("D", "X", 9),
    Formation("D", "X", 10)
]
affiche_liste_Formation(test)
print("\nMédiane calculée :", mediane_niveau(test))  #5.5


#TEST 6 : liste très grande
print("---------------------------------------------------------------------------")
print("TEST 6 :")
print("Cas d'une liste très grande (10000 éléments)\n")

test = []
for i in range(10000):
    test.append(Formation("Science", "info", i + 1))  # niveaux de 1 à 10000

print("\nMédiane calculée :", mediane_niveau(test))  #5000.5

