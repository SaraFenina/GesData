"""
    Auteur: Sara Fenina
    Crée le 07/03/2025
    PARTIE 1 : Semaine 1
    Fonctions de test du fichier SF_00_type de la fonction affiche_Formation
"""


#imporation du fichier SF_00_type
from SF_00_type import*



#TEST 1
print("bonjour voici un programme de test pour la fonction Fromation")
print("------------------------------------------------------------------------------------------------------------------------------")
print("\nVoici le TEST 1 : celui de l'affichage d'un apprantis qui est dans le SOCIAL (str) qui suit la formation d'AIDE-SOIGNANT (str) avec un niveau de formation de 4 (int)")
print("IL est attendu d'avoir Le domaine de l'apprentis est dans le social"
      "La formation de l'apprantis est aide-soignant"
      "Le niveau de fomation de l'apprantis est 4  affichée")

forma=Formation("social","aide-soignant",4)
affiche_Formation(forma)




#TEST 2
print("------------------------------------------------------------------------------------------------------------------------------")
print("\nVoici le TEST 2 : celui de l'affichage d'un apprantis qui est dans le SANITAIRE(str) qui suit la formation d'ASSISTANT FAMILIAL(str) avec un niveau de formation de 1 (int)")
print("IL est attendu d'avoir Le domaine de l'apprentis est dans le sanitaire"
      "La formation de l'apprantis est Assistant familial"
      "Le niveau de fomation de l'apprantis est 1 affichée")

forma=Formation("sanitaire","Assistant familial",1)
affiche_Formation(forma)



#TEST 3
print("------------------------------------------------------------------------------------------------------------------------------")
print("\nVoici le TEST 3 : celui de l'affichage d'un apprantis qui est dans le SANITAIRE(str) qui suit la formation d'ASSISTANT FAMILIAL(str) avec un niveau de formation de 1(str)")
print("IL est attendu d'avoir Le domaine de l'apprentis est dans le sanitaire"
      "La formation de l'apprantis est Assistant familial"
      "Le niveau de fomation de l'apprantis est 1  affichée")

forma=Formation("sanitaire","Assistant familial","1")
affiche_Formation(forma)
