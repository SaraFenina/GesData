"""
    Auteur : Sara Fenina
    Crée le 07/04/2025
    PARTIE 2 Semaine 1
    Programme TEST de la fonction tri_selection qui se trouve dans SF_02_listes_type
"""


from SF_02_listes_type import *
#TEST 1 Liste vide
print("Programme de test de la fonction tri_selection")
print("--------------------------------------------------")
print("TEST 1 : Liste vide")
test = []
taille_avant = len(test)
print("Liste avant d'être triée : ", test, "\n")
print("Est triée ?", est_triee(test)) #True
tri_selection(test)
print("Liste triée :", test)
print("Est triée ?", est_triee(test))  #True
print("Longueur conservée ?", taille_avant == len(test))


# TEST 2 : Liste avec un seul élément
print("--------------------------------------------------")
print("TEST 2 : Un seul élément")
test = [Formation("Science", "Maths", 10)]
taille_avant = len(test)
print("Liste avant d'être triée : \n")
affiche_liste_Formation(test)
print("\n------> Est triée ?", est_triee(test)) #True
tri_selection(test)
print("\n-------------------------")
print("Liste après d'être triée : \n")
affiche_liste_Formation(test)
print("\n------> Est triée ?", est_triee(test)) #True
print("Longueur conservée ?", taille_avant == len(test))


# TEST 3 : Liste non triée
print("--------------------------------------------------")
print("TEST 3 : Liste non triée")
test = [
    Formation("Science", "Physique", 5),
    Formation("Science", "Maths", 1),
    Formation("Science", "Chimie", 9)
]
taille_avant = len(test)
print("Liste avant d'être triée : \n")
affiche_liste_Formation(test)
print("\n------> Est triée ?", est_triee(test)) #False
tri_selection(test)
print("\n-------------------------")
print("Liste après d'être triée : \n")
affiche_liste_Formation(test)
print("\n------> Est triée ?", est_triee(test)) #True
print("Longueur conservée ?", taille_avant == len(test))


# TEST 4 : Liste déjà triée
print("--------------------------------------------------")
print("TEST 4 : Liste déjà triée")
test = [
    Formation("Science", "Maths", 1),
    Formation("Science", "Physique", 5),
    Formation("Science", "Chimie", 9)
]
taille_avant = len(test)
print("Liste avant d'être triée : \n")
affiche_liste_Formation(test)
print("\n------> Est triée ?", est_triee(test)) #True
tri_selection(test)
print("\n-------------------------")
print("Liste après d'être triée : \n")
affiche_liste_Formation(test)
print("\n------> Est triée ?", est_triee(test))  #True
print("Longueur conservée ?", taille_avant == len(test))
