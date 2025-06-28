"""
    Auteur: Sara Fenina
    Crée le 16/04/2025
    PARTIE 2 : Semaine 2
    Fonction de mesure de temp des fonction :
                                             nombre_occurrences_niveau
                                             recherche_grand_niveau
                                             recherche_petit_niveau
                                             recherche_dicho_niveau
    Contient fonction :
                    mesurer_courbe
                    mesurer_complexite_lineaire
                    mesurer_comlexite_logarithmique
"""
                    


# import pour mesurer le temps d'exécution d'une fonction donnée
import timeit
import math
from outils_dessin import *
from outils_mesure import *
from SF_02_listes_type import *
from SF_fonction_en_plus import *

print("Ci-dessous un dessin du temps d'exécution de différentes fonctions pour différentes tailles de liste.")
print("------> L'apparition prendra jusqu'à 15~~30 secondes\n")
input("Veuillez appuyer sur entrée pour continuer, puis fermer la fenêtre pop-up pour continuer les autres cas.")

# Liste des fonctions à tester
noms_fonctions = ["recherche_dicho_niveau", "recherche_grand_niveau", "recherche_petit_niveau", "nombre_occurrences_niveau"]

# Paramètres des répétitions et initialisation
nb_repet = 1




# Fonction pour mesurer le temps d'exécution d'une fonction donnée ( choisi par la liste des fonction a testé )
def mesurer_courbe(fonction, longueur_max, pas_longueur):
    """
    Rôle : Calculer le temp d'execution des fonction "nombre_occurrences_niveau", "recherche_grand_niveau", "recherche_petit_niveau", "recherche_dicho_niveau"
    Type de Données:
        lforma : liste de valuer de type Formation
        fonction : une fonction python
        longeur_max : nombre 
        pas_longeur : float
    Type de Resultat :
        courbe_temp : liste de couple 
    """
    
    courbe_temp = []

    for longueur in range(1, longueur_max + 1, pas_longueur):
        # Création de la chaîne d'instructions pour mesurer le temps d'exécution en la gardant en STR
        instructions_initialisation = """
from SF_02_listes_type import nombre_occurrences_niveau, recherche_grand_niveau, recherche_petit_niveau, recherche_dicho_niveau
from __main__ import Formation
valeur = """ + str(longueur // 2) + """
lforma = []
for i in range(""" + str(longueur) + """):  
    lforma.append(Formation("Science", "Maths",i ))
"""

        instructions_a_mesurer = """
variable = """ + fonction + """(lforma,valeur)

"""


        

        # Mesure du temps d'exécution
        temps = timeit.timeit(stmt=instructions_a_mesurer,
                              setup=instructions_initialisation,
                              number=nb_repet)
        temps = temps_en_nanoseconde(temps / nb_repet)*(10**-2)
        courbe_temp.append((longueur, temps))

       

    return courbe_temp




def mesurer_comlexite_logarithmique(longueur_max,k,pas_longueur):
    """
    Rôle : Calculer le temp d'execution d'une fonction logarithmique
    Type de Données:
        k : nombre : coeffition directeur d'une droite
        pas_longeur : float : unité d'affichage
    Type de Resultat :
        courbe_temp : liste de couple
    """
    courbe=[]
    for longueur in range(1, longueur_max + 1, pas_longueur):
        temp = math.log(longueur + 1) * k 
        courbe.append((longueur, temp))
    return courbe



for i in range(len(noms_fonctions)):
    print("--------------------------------------------------------------------------------------")
    print("Voici la courbe du temps d'exécution de la fonction", noms_fonctions[i])

    # Explication des couleurs des courbes avant le pop-up
    print("\nExplication des couleurs des courbes :")
    print("Courbe bleue : correspond aux tests avec des listes de taille allant jusqu'à 500000 éléments.")
    print("courbe verte : correspond à la complexité logarithmique . Courbe de reference ")
    
    # Initialisation des courbes
    courbe_bleue = []
    courbe_verte=[]


    # Paramètres des courbes
    longueur_max_bleue = 500000
    longueur_max_vert = 500000

    k = 10

    # Initialisation des unité d'affichage
    pas_longueur_bleue = 2000
    pas_longueur_verte = 10000


    # Calcul des courbes
    courbe_bleue = mesurer_courbe(noms_fonctions[i], longueur_max_bleue, pas_longueur_bleue)
    courbe_verte = mesurer_comlexite_logarithmique(longueur_max_vert,k,pas_longueur_verte)
   

    # Dessiner les trois courbes ensemble en fonction de la taille de luste
    dessine_lignes_brisees(courbe_bleue=courbe_bleue,
                           courbe_verte=courbe_verte)

    input("\nAppuyez sur entrée pour continuer.")

    i = i + 1

print("Fin du programme.")
