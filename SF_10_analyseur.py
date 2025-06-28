"""
    Auteur : Sara Fenina
    Crée le 21/03/2025
    PARTIE 1 :Semaine 3
    Contient : le programme principal

                        
"""

from SF_02_listes_type import*
from outils_csv import*
from SF_fonction_en_plus import *


def menu():
    """Menu interactif pour l'utilisateur."""
    lforma = []  
    choix = ""
    while choix != "5":
        print("\nMenu :")
        print("1. Ouvrir un fichier")
        print("2. Filtrer les données")
        print("3. Afficher les statistiques")
        print("4. Rechercher des occurrences")
        print("5. Quitter")
        
        choix = input("Choisissez une option : ")
        

        if choix == "1":
            fichiers = ["DONNEES/SF_data_0.csv", "DONNEES/SF_data_1.csv", "DONNEES/SF_data_5.csv", "DONNEES/SF_data_20.csv", "DONNEES/SF_data_100.csv","DONNEES/SF_data_initial.csv"]
            taille = [0,1,5,20,100,414]

            print("Liste des fichiers disponibles :")
            for i in range(len(fichiers)):
                print("Choisir ",str(i+1)," pour Fichier : ",fichiers[i]," de tailles ",str(taille[i]))

            est_valide = False
    
            while not est_valide:
                choix_fichier = input("\nChoisissez un fichier en entrant l'indice de 1 à " + str(len(fichiers)) + " :\n")
        
    
                if verif_choix(choix_fichier, len(fichiers)):
                    fichier_choisi = fichiers[int(choix_fichier) - 1] 
                    print("Vous avez choisi le fichier :", fichier_choisi)
                    est_valide = True
                else:
                    print("Choix invalide. Veuillez entrer un numéro entre 1 et", len(fichiers))
    
 
            (liste_entete, liste_donnees) = lecture_fichier_csv(fichier_choisi, ";", "utf-8", 1)
           
            if len(liste_donnees) == 0:
                print("La liste des données est vide. Aucun affichage effectué.")
            else:
                lforma = []  
                lforma=transformation_chaine_forma(liste_donnees, lforma)
                print("Donnée chargée")
            

        
        


        
        if choix == "2":
            critere_trouve = False

            while not critere_trouve:
                critere = input("Entrez le critère de filtrage (domaine ex:social ou formation : exp Educateur Spécialisé ) : ")
        
                if verif_critere(critere):  
                    lforma_filtre = filtrer(lforma, critere)  

                    if len(lforma_filtre) > 0:  
                        critere_trouve = True
                        lforma=lforma_filtre
                        if len(lforma)<100 :
                            affiche_liste_Formation(lforma)
                        else:
                            print("\nLa taille de la liste de données est supperieur a 100 , elle sera donc pas affiché \n")
                    else: 
                        print("\nLe critère n'a pas été trouvé.\n")
                        critere_trouve=True
                else:
                    print("\nLe critère doit être non numérique. Veuillez réessayer.\n")

            
            


        
        if choix == "3":
           if len(lforma) > 0:
               if not est_triee(lforma):
                   print("-----------------")
                   print("La liste n'est pas triée. Tri en cours...")
                   tri_selection(lforma)
               if len(lforma)<len(liste_donnees):
                   print("\n--------")
                   print("PS : Le nombre d'enregistrement sera inferieur à la taille de données initial pour cause de presence de ligne vide dans le jeux de données choisi")
               affiche_statistiques(lforma)

           else:
               print("Le fichier est vide , pas de statistique a afficher")


        if choix == "4":
            
            if not est_triee(lforma):
                print("-----------------")
                print("La liste n'est pas triée. Tri en cours...")
                tri_selection(lforma)

    
            valeur =input("Entrez une valeur numérique à rechercher (niveau): ")
            nb_occurrences = nombre_occurrences_niveau(lforma, int(valeur))   
            print("Le nombre d'occurrences de ",valeur," est : ",nb_occurrences)

            
        if choix =="5":
            print("Fin Du Programme ")
            
        if choix!="1" and choix!="2" and choix!="3" and choix!="4" and choix!="5":
            print("Option invalide, veuillez réessayer.")









    
menu()











