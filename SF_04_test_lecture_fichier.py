"""
    Auteur : Sara Fenina
    Crée le 07/03/2025
    PARTIE 1 : Semaine 1
    Fonction de test du fichier SF_02_listes_type de la fonction transforme_liste_chaine
"""

#importation de la fonction de lecture d'un fichier csv
from outils_csv import *
from SF_02_listes_type import *



# Exemple de test 1 avec vérification
nom_fichier = "DONNEES/SF_data_0.csv"
(liste_entete, liste_donnees) = lecture_fichier_csv(nom_fichier, ";", "utf-8", 1)
print("Voici TEST 1 : test fonction transformation avec le fichier SF_data_0\n")
if len(liste_donnees) == 0:
    print("La liste des données est vide. Aucun affichage effectué.") #attendu d'avoir ce print
else:
    nombre_ligne = len(liste_donnees)
    print("Le nombre de lignes de données contenues dans le fichier est de", nombre_ligne)
    if 0 < len(liste_donnees) < 18:
        print("Voici les élements qui se trouvent dans la liste : \n")
        lforma = []  # Initialisation de la liste lforma
        lforma=transformation_chaine_forma(liste_donnees, lforma)
        affiche_liste_Formation(lforma)  
    else:
        print("Le nombre d'éléments dans la liste est supérieur ou égal à 18. Aucun affichage.")




# TEST 2
print("-----------------------------------------------------------------------------------------------------------")
nom_fichier = "DONNEES/SF_data_1.csv"
liste_entete, liste_donnees = lecture_fichier_csv(nom_fichier, ";", "utf-8", 1)
print("Voici TEST 2 : test fonction transformation avec le fichier SF_data_1\n")
if len(liste_donnees) == 0:
    print("La liste des données est vide. Aucun affichage effectué.")
else:
    nombre_ligne = len(liste_donnees)
    print("Le nombre de lignes de données contenues dans le fichier est de", nombre_ligne) #1 et la liste de donnee
    
    if 0 < len(liste_donnees) < 18:
        print("Voici les élements qui se trouvent dans la liste : \n")
        lforma = []  # Initialisation de la liste lforma
        lforma=transformation_chaine_forma(liste_donnees, lforma)
        affiche_liste_Formation(lforma)  
    else:
        print("Le nombre d'éléments dans la liste est supérieur ou égal à 18. Aucun affichage.")
# TEST 3
print("-----------------------------------------------------------------------------------------------------------")
nom_fichier = "DONNEES/SF_data_5.csv"
liste_entete, liste_donnees = lecture_fichier_csv(nom_fichier, ";", "utf-8", 1)
print("Voici TEST 3 : test fonction transformation avec le fichier SF_data_5\n")
if len(liste_donnees) == 0:
    print("La liste des données est vide. Aucun affichage effectué.")
else:
    nombre_ligne = len(liste_donnees)
    print("Le nombre de lignes de données contenues dans le fichier est de", nombre_ligne) #5 et la liste de donnee

    if 0 < len(liste_donnees) < 18:
        print("Voici les élements qui se trouvent dans la liste : \n")
        lforma = []  # Initialisation de la liste lforma
        lforma=transformation_chaine_forma(liste_donnees, lforma)
        affiche_liste_Formation(lforma)
      
    else:
        print("Le nombre d'éléments dans la liste est supérieur ou égal à 18. Aucun affichage.")

# TEST 4
print("-----------------------------------------------------------------------------------------------------------")
nom_fichier = "DONNEES/SF_data_20.csv"
liste_entete, liste_donnees = lecture_fichier_csv(nom_fichier, ";", "utf-8", 1)
print("Voici TEST 4 : test fonction transformation avec le fichier SF_data_20\n")
if len(liste_donnees) == 0:
    print("La liste des données est vide. Aucun affichage effectué.")
else:
    nombre_ligne = len(liste_donnees)
    print("Le nombre de lignes de données contenues dans le fichier est de", nombre_ligne) 

    if 0 < len(liste_donnees) < 18:
        print("Voici les élements qui se trouvent dans la liste : \n")
        lforma = []  # Initialisation de la liste lforma
        lforma=transformation_chaine_forma(liste_donnees, lforma)
        affiche_liste_Formation(lforma)  
    else:
        print("Le nombre d'éléments dans la liste est supérieur ou égal à 18. Aucun affichage.")#20 et ce print


# TEST 5
print("-----------------------------------------------------------------------------------------------------------")
nom_fichier = "DONNEES/SF_data_100.csv"
liste_entete, liste_donnees = lecture_fichier_csv(nom_fichier, ";", "utf-8", 1)
print("Voici TEST 5 : test fonction transformation avec le fichier SF_data_100\n")
if len(liste_donnees) == 0:
    print("La liste des données est vide. Aucun affichage effectué.")
else:
    nombre_ligne = len(liste_donnees)
    print("Le nombre de lignes de données contenues dans le fichier est de", nombre_ligne)

    if 0 < len(liste_donnees) < 18:
        print("Voici les élements qui se trouvent dans la liste : \n")
        lforma = []  # Initialisation de la liste lforma
        lforma=transformation_chaine_forma(liste_donnees, lforma)
        affiche_liste_Formation(lforma)  
    else:
        print("Le nombre d'éléments dans la liste est supérieur ou égal à 18. Aucun affichage.")#100 et ce print
