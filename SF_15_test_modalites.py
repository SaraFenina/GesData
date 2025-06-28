"""
    Auteur : Sara Fenina
    Crée le 07/04/2025
    PARTIE 2 : Semaine 1
    Programme de test de la fonction modalites_niveau qui se trouve dans le fichier SF_02_listes_type
"""



from SF_02_listes_type import *

# Programme de test pour la fonction modalites_niveau

# TEST 1 : Liste vide
print("--------------------------------------------------")
print("TEST 1 : Liste vide")
test = []
modalites = modalites_niveau(test)
affiche_liste_Formation(test)

print("\nModalités :", modalites)  # Résultat attendu : []

# TEST 2 : Une seule modalité
print("--------------------------------------------------")
print("TEST 2 : Une seule modalité")
test = [
    Formation("Science", "Physique", 4),
    Formation("Science", "Maths", 4),
    Formation("Social", "Psycho", 4)
]
modalites = modalites_niveau(test)
affiche_liste_Formation(test)

print("\nModalités :", modalites)  # Résultat attendu : [4]

# TEST 3 : Plusieurs modalités triées
print("--------------------------------------------------")
print("TEST 3 : Plusieurs modalités triées")
test = [
    Formation("Science", "Biologie", 1),
    Formation("Science", "Chimie", 2),
    Formation("Science", "Maths", 2),
    Formation("Social", "Psycho", 5),
    Formation("Social", "Socio", 7),
    Formation("Social", "Eco", 9)
]
modalites = modalites_niveau(test)
affiche_liste_Formation(test)

print("\nModalités :", modalites)  # Résultat attendu : [1, 2, 5, 7, 9]

# TEST 4 : Liste avec valeurs répétées au début et à la fin
print("--------------------------------------------------")
print("TEST 4 : Répétitions début et fin")
test = [
    Formation("Science", "Biologie", 1),
    Formation("Science", "Biologie", 1),
    Formation("Science", "Chimie", 3),
    Formation("Science", "Chimie", 3),
    Formation("Science", "Chimie", 3),
    Formation("Social", "Psycho", 7),
    Formation("Social", "Eco", 9),
    Formation("Social", "Eco", 9)
]
modalites = modalites_niveau(test)
affiche_liste_Formation(test)

print("\nModalités :", modalites)  # Résultat attendu : [1, 3, 7, 9]


