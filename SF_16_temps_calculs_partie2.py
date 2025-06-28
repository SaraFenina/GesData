"""
    Auteur: Sara Fenina
    Crée le 10/10/2025
    PARTIE 2 : Semaine 1
    Fonction de mesure de temp des fonction :
                                             tri_selection
                                             est_triee
                                             modalites_niveau
                                             mediane_niveau
    Contient fonction :
                    mesurer_courbe
                    mesurer_complexite_lineaire
                    mesurer_complexité_quadratique
"""
                    


# import pour mesurer le temps d'exécution d'une fonction donnée
import timeit
from outils_dessin import *
from outils_mesure import *
from SF_02_listes_type import *
from SF_fonction_en_plus import *

print("Ci-dessous un dessin du temps d'exécution de différentes fonctions pour différentes tailles de liste.")
print("------> L'apparition prendra jusqu'à 15~~60 secondes\n")
input("Veuillez appuyer sur entrée pour continuer, puis fermer la fenêtre pop-up pour continuer les autres cas.")

# Liste des fonctions à tester
noms_fonctions = ["mediane_niveau", "modalites_niveau", "est_triee", "tri_selection"]

# Paramètres des répétitions et initialisation
nb_repet = 1




# Fonction pour mesurer le temps d'exécution d'une fonction donnée ( choisi par la liste des fonction a testé )
def mesurer_courbe(fonction, longueur_max, pas_longueur):
    """
    Rôle : Calculer le temp d'execution des fonction "modalites_niveau", "mediane_niveau", "tri_selection", "est_triee"
    Type de Données:
        lforma : liste de valuer de type Formation
        fonction : une fonction python
        longueur_max : nombre 
        pas_longueur : float
    Type de Resultat :
        courbe_temp : liste de couple 
    """
    
    courbe_temp = []
           
    for longueur in range(1, longueur_max + 1, pas_longueur):
        # Création de la chaîne d'instructions pour mesurer le temps d'exécution en la gardant en STR
        instructions_initialisation = """
from SF_02_listes_type import est_triee, tri_selection, mediane_niveau, modalites_niveau
from __main__ import Formation
lforma = []
for i in range(""" + str(longueur) + """):  
    lforma.append(Formation("Science", "Maths", i))
"""
    

        instructions_a_mesurer = """
variable = """ + fonction + """(lforma)
"""


        

        # Mesure du temps d'exécution
        temps = timeit.timeit(stmt=instructions_a_mesurer,
                              setup=instructions_initialisation,
                              number=nb_repet)
        temps = temps_en_nanoseconde(temps / nb_repet) 
        courbe_temp.append((longueur, temps))

      

    return courbe_temp



# Fonction pour mesurer le temp d'exécution d'une fonction lineaire
def mesurer_complexite_lineaire(longueur_max, k, pas_longueur):
    """
    Rôle : Calculer le temp d'execution d'une fonction lineaire n → kn
    Type de Données:
        k : nombre : coeffition directeur d'une droite
        pas_longueur : float : unité d'affichage
    Type de Resultat :
        courbe_temp : liste de couple
    """
    courbe = []
    for longueur in range(1, longueur_max + 1, pas_longueur):
        temps = longueur * k 
        courbe.append((longueur, temps))
    return courbe

def mesurer_complexité_quadratique(longueur_max, k, pas_longueur):
    """
    Rôle : Calculer le temp d'execution d'une fonction quadratique x**2
    Type de Données:
        k : nombre : coeffition directeur d'une droite
        pas_longueur : float : unité d'affichage
    Type de Resultat :
        courbe_temp : liste de couple
    """
    courbe = []
    for longueur in range(1, longueur_max + 1, pas_longueur):
        temp = (longueur ** 2) * k 
        courbe.append((longueur, temp))
    return courbe

for i in range(len(noms_fonctions)):
    print("--------------------------------------------------------------------------------------")
    print("Voici la courbe du temps d'exécution de la fonction", noms_fonctions[i])

    # Explication des couleurs des courbes avant le pop-up
    print("\nExplication des couleurs des courbes :")
    print("Courbe rouge : correspond à la complexité linéaire. Courbe de réferance ")
    print("Courbe bleue : correspond aux tests avec des listes de taille allant jusqu'à 500000 éléments.")
    print("---->Sauf pour la fonction tri_selection qui sera jusqu'à 10000 éléments.")
    print("Courbe verte : correspond à la complexité quadratique . courbe de réference ")
   
    
    # Initialisation des courbes
    courbe_rouge = []
    courbe_bleue = []
    courbe_verte = []

    # Paramètres des courbes
    # Paramètres personnalisés selon la fonction
    if noms_fonctions[i] == "tri_selection":
        k_lineaire = 0
        k_quadratique = 15
        longueur_max_rouge = 10000
        pas_longueur_rouge = 1000
        longueur_max_bleue = 10001     
        pas_longueur_bleue = 2000      
        longueur_max_verte = 10001
        pas_longueur_verte = 2000

    elif noms_fonctions[i] == "mediane_niveau":
        k_lineaire = 250 * (10**-4) 
        k_quadratique = 0
        longueur_max_rouge = 500000
        pas_longueur_rouge = 10000
        longueur_max_bleue = 500000
        pas_longueur_bleue = 4500
        longueur_max_verte = 1000
        pas_longueur_verte = 100
    else:
        k_lineaire = 250
        k_quadratique = 0
        longueur_max_rouge = 500000
        pas_longueur_rouge = 10000
        longueur_max_bleue = 500000
        pas_longueur_bleue = 5000
        longueur_max_verte = 500000
        pas_longueur_verte = 10000



    # Calcul des courbes
    #obligation de creer une fonction pour pourvoir affecter son resultat pour etre capable d'avoir 3 courbe differente 
    courbe_rouge = mesurer_complexite_lineaire(longueur_max_rouge, k_lineaire, pas_longueur_rouge)
    courbe_bleue = mesurer_courbe(noms_fonctions[i], longueur_max_bleue, pas_longueur_bleue)
    courbe_verte = mesurer_complexité_quadratique(longueur_max_verte, k_quadratique, pas_longueur_verte)

    # Dessiner les trois courbes ensemble en fonction de la taille de luste
    dessine_lignes_brisees(courbe_rouge=courbe_rouge,
                           courbe_bleue=courbe_bleue,
                           courbe_verte=courbe_verte)

    input("\nAppuyez sur entrée pour continuer.")

    i = i + 1

print("Fin du programme.")
