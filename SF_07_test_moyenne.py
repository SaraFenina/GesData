"""
    Auteur : Sara Fenina
    Crée le 19/03/2025
    PARTIE 1 : Semaine 2
    Fonction test de la fonction moyenne_niveau dans SF_02_listes_type
"""

from SF_02_listes_type import*

#TEST 1 : cas general
print("---------------------------------------------------------------------------")
print("TEST 1 :")
print("Cas general de l'utilisation de la fonction moyenne\n")
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 95)]
print(moyenne_niveau(test)) #il est attendu d'avoir 27.0





#TEST 2 : valeur identique 
print("---------------------------------------------------------------------------")
print("TEST 2 :")
print("Cas valeur identique dans l'utilisation de la fonction moyenne\n")
test=[
    Formation("Science", "Maths", 15),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 15),
    Formation("Science", "Informatique", 15),
    Formation("Lettres", "Philosophie", 15)]

print(moyenne_niveau(test))#15.0


#TEST 3 : un seul element
print("---------------------------------------------------------------------------")
print("TEST 3 :")
print("Cas un seul element dans l'utilisation de la fonction moyenne\n")
test= [Formation("Science", "Maths", 42)]
print(moyenne_niveau(test))#42.0

#TEST 4 : element au debut
print("---------------------------------------------------------------------------")
print("TEST 4 :")
print("Cas un  element au debut dans l'utilisation de la fonction moyenne\n")
test=[
    Formation("Science", "Maths", 5),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 35),
    Formation("Science", "Informatique", 25),
    Formation("Lettres", "Philosophie", 45)]
print(moyenne_niveau(test)) #25


#TEST 5 : element a la fin
print("---------------------------------------------------------------------------")
print("TEST 5 :")
print("Cas un  element a la fin dans l'utilisation de la fonction moyenne\n")
test=[
    Formation("Science", "Maths", 45),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 35),
    Formation("Science", "Informatique", 25),
    Formation("Lettres", "Philosophie", 5)]
print(moyenne_niveau(test)) #25


#TEST 6 : liste très grande
print("---------------------------------------------------------------------------")
print("TEST 6 :")
print("Cas d'une liste très grande (10000 éléments)\n")

test = []
for i in range(10000):
    test.append(Formation("Science", "info", i + 1))  # niveaux de 1 à 10000

print(moyenne_niveau(test)) #5000.5
