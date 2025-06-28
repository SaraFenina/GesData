"""
    Auteur:" Sara Fenina "
    Crée le 19/03/2025
    PARTIE 1 : semaine 2
    Fonction test du fichier FILTRE de la fonction filtrer
"""


from SF_02_listes_type import*


#TEST 1
print("---------------------------------------------------------------------------")
print("TEST 1 : Cas général 1")
print("On cherche les formations du DOMAINE 'Science'.\n")
test_filtree=[]
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 95)]

test_filtree=filtrer(test, "Science")
affiche_liste_Formation(test_filtree) #Il est attendu de voir les 4 premiere valeur de test 


#TEST 2
print("---------------------------------------------------------------------------")
print("TEST 2 : Cas général 2")
print("\nOn cherche la FORMATION 'Philosophie'.\n")
test_filtree=[]
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 95)]
test_filtree=filtrer(test, "Philosophie")
affiche_liste_Formation(test_filtree) #"Lettres", "Philosophie", 95

#TEST 3
print("---------------------------------------------------------------------------")
print("TEST 3 : Liste vide")
print("On teste la fonction avec une liste vide.\n")
test_filtree=[]
test = []
test_filtree=filtrer(test, "Science")
affiche_liste_Formation(test_filtree)  #Aucune Formation

#TEST 4
print("---------------------------------------------------------------------------")
print("TEST 4 : Aucun élément correspondant")
print("On cherche un domaine ou une formation qui n'existe pas ('Musique').\n")
test_filtree=[]
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 95)]

test_filtree=filtrer(test, "Musique")
affiche_liste_Formation(test_filtree)   #Aucune Formation


#TEST 5

print("---------------------------------------------------------------------------")
print("TEST 5 : Valeurs identiques")
print("Toutes les formations appartiennent au même domaine 'Science'.\n")
test_filtree=[]
test = [
    Formation("Science", "Maths", 15),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 15),
    Formation("Science", "Informatique", 15),
    Formation("Science", "Biologie", 15)
]

test_filtree=filtrer(test, "Science")
affiche_liste_Formation(test_filtree) # Tout test
