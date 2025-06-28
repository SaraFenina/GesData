"""
    Auteur : Sara Fenina
    Crée le 19/03/2025
    PARTIE 1 : Semaine 2
    Fonction test de la fonction ecart_type_niveau dans SF_02_listes_type
"""

from SF_02_listes_type import*

#TEST 1 : cas general
print("---------------------------------------------------------------------------")
print("TEST 1 :")
print("Cas général de l'utilisation de la fonction ecart_type\n")
test = [
    Formation("Science", "Maths", 10),
    Formation("Science", "Physique", 10),
    Formation("Science", "Chimie", 10),
    Formation("Science", "Informatique", 10),
    Formation("Lettres", "Philosophie", 95)]
print(ecart_type_niveau(test))  # écart-type attendu : autour de 34.0


#TEST 2 : valeurs identiques
print("---------------------------------------------------------------------------")
print("TEST 2 :")
print("Valeurs identiques dans la liste\n")
test = [
    Formation("Science", "Maths", 15),
    Formation("Science", "Physique", 15),
    Formation("Science", "Chimie", 15),
    Formation("Science", "Informatique", 15),
    Formation("Lettres", "Philosophie", 15)]
print(ecart_type_niveau(test))  # écart-type attendu : 0.0

#TEST 3 : un seul élément
print("---------------------------------------------------------------------------")
print("TEST 3 :")
print("Un seul élément dans la liste\n")
test = [Formation("Science", "Maths", 42)]
print(ecart_type_niveau(test))  # écart-type attendu : 0.0

#TEST 4 : moitié des valeurs valent 2x, moitié valent 0 avec x=20
print("---------------------------------------------------------------------------")
print("TEST 4 :")
print("Moitié des valeurs valent 2x, l'autre moitié valent 0 (x=20)\n")
x = 20
test = [
    Formation("Science", "Maths", 2 * x),
    Formation("Science", "Physique", 2 * x),
    Formation("Science", "Chimie", 2 * x),
    Formation("Science", "Informatique", 0),
    Formation("Lettres", "Philosophie", 0),
    Formation("Lettres", "Philosophie", 0)]
print(ecart_type_niveau(test))  # écart-type attendu : (20)


#TEST 5 : valeur negative
print("---------------------------------------------------------------------------")
print("TEST 5 :")
print("Valeur negative dans la liste \n")
test = [
    Formation("Science", "Physique", -10),
    Formation("Science", "Informatique", -20),
    Formation("Science", "Philosophie", -30)]
print(ecart_type_niveau(test))  # écart-type attendu :  positif (~8.16)

#TEST 6 : liste très grande
print("---------------------------------------------------------------------------")
print("TEST 6 :")
print("Cas d'une liste très grande (10000 éléments)\n")

test = []
for i in range(10000):
    test.append(Formation("Science", "info", i + 1))  # niveaux de 1 à 10000
print(ecart_type_niveau(test)) # (~2886.75)

