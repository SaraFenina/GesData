"""
    Auteur : Sara Fenina
    Crée le 07/03/2025
    PARTIE 1 : Semaine 1
    Fonction de test du fichier SF_02_listes_type de la fonction affiche_liste_Formation
"""

from SF_02_listes_type import*

#TEST 1
print("bonjour voici un programme de test pour la fonction Fromation")
print("------------------------------------------------------------------------------------------------------------------------------")
print("\nVoici le TEST 1 : affichage du contenu de la liste lforma ")
print("-------------> lforma=[Formation('social','aide-soignant',4)",
        "\n                       Formation('Social','assistant familial',0)]")
print("Le resultats attendu est\n",
      "\nLe domaine de l'apprentis est dans le social",
      "\nLa formation de l'apprantis est aide-soignant")
print("\nLe niveau de fomation de l'apprentis est 4",
      "\nLe domaine de l'apprentis est dans le Social",
      "\nLa formation de l'apprentis est assistant familial",
      "\nLe niveau de fomation de l'apprantis est 0")

print("---------------------------------------------")
print("Voici ce qui est affichée")
lforma=[Formation("social","aide-soignant",4),
        Formation("Social","assistant familial",0)]
affiche_liste_Formation(lforma)



#TEST 2
print("------------------------------------------------------------------------------------------------------------------------------")
print("\nVoici le TEST 2 : affichage du contenu de la liste vide 'lforma' ")
print("Le resultats attendu est 'Aucune Formation' ")

print("---------------------------------------------")
print("Voici ce qui est affichée")
lforma=[]
affiche_liste_Formation(lforma)


#TEST 3
print("------------------------------------------------------------------------------------------------------------------------------")
print("\nVoici le TEST 3 : affichage du contenu de la liste  'lforma' =[Formation('social','aide-soignant',4)] ")
print("Le resultats attendu est\n",
      "\nLe domaine de l'apprentis est dans le social",
      "\nLa formation de l'apprantis est aide-soignant",
      "\nLe niveau de fomation de l'apprentis est 4")

print("---------------------------------------------")
print("Voici ce qui est affichée")
lforma=[Formation("social","aide-soignant",4)]
affiche_liste_Formation(lforma)



