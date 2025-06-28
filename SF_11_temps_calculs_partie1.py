"""
    Auteur: Sara Fenina
    Crée le 28/03/2025
    PARTIE 1 : Semaine 4
    Fonction de mesure de temp des fonction :
                                             minimum_niveau
                                             maximum_niveau
                                             moyenne_niveau
                                             ecart_type_niveau
    Contient fonction :
                    mesurer_courbe
                    mesurer_complexite_lineaire
"""
                    


# import pour mesurer le temps d'exécution d'une fonction donnée
import timeit
from outils_dessin import *
from outils_mesure import *
from SF_02_listes_type import *
from SF_fonction_en_plus import *

print("Ci-dessous un dessin du temps d'exécution de différentes fonctions pour différentes tailles de liste.")
print("------> L'apparition prendra jusqu'à 15 secondes\n")
input("Veuillez appuyer sur entrée pour continuer, puis fermer la fenêtre pop-up pour continuer les autres cas.")


# Liste des fonctions à tester
noms_fonctions = ["minimum_niveau", "maximum_niveau", "moyenne_niveau", "ecart_type_niveau"]

# Paramètres des répétitions et initialisation
nb_repet = 1


instructions_initialisation = """
from SF_02_listes_type import minimum_niveau, maximum_niveau, moyenne_niveau, ecart_type_niveau
from __main__ import Formation  
"""



# Fonction pour mesurer le temps d'exécution d'une fonction donnée ( choisi par la liste des fonction a testé )
def mesurer_courbe(fonction, longueur_max, pas_longueur,nb_repet):
    """
    Rôle : Calculer le temp d'execution des fonction "minimum_niveau", "maximum_niveau", "moyenne_niveau", "ecart_type_niveau"
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
        instructions_a_mesurer = """
lforma = []
for i in range(""" + str(longueur) + """):  
    lforma.append(Formation("Science", "Maths", 10))
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
def mesurer_complexite_lineaire(longueur_max, k, pas_longueur,nb_repet):
    """
    Rôle : Calculer le temp d'execution d'une fonction lineaire n → kn
    Type de Données:
        k : nombre : coeffition directeur d'une droite
        pas_longeur : float : unité d'affichage
    Type de Resultat :
        courbe_temp : liste de couple
    """
    courbe = []
    for longueur in range(1, longueur_max + 1, pas_longueur):
        temps = longueur * k
        courbe.append((longueur, temps))
    return courbe


for i in range(len(noms_fonctions)):
    print("--------------------------------------------------------------------------------------")
    print("Voici la courbe du temps d'exécution de la fonction", noms_fonctions[i])
    

    # Explication des couleurs des courbes avant le pop-up
    print("\nExplication des couleurs des courbes :")
    print("Courbe rouge : correspond à la complexité linéaire. Courbe de réference ")
    print("Courbe bleue : correspond aux tests avec des listes de taille allant jusqu'à 500000 éléments.")
    
    
    # Initialisation des courbes
    courbe_rouge = []
    courbe_bleue = []
    
    # Paramètres des courbes
    longueur_max_rouge = 500000
    longueur_max_bleue = 500000

    k = 250

    # Initialisation des unité d'affichage
    pas_longueur_rouge = 10000
    pas_longueur_bleue = 2000


    # Calcul des courbes
    #obligation de creer une fonction pour pourvoir affecter son resultat pour etre capable d'avoir 3 courbe differente 
    courbe_rouge = mesurer_complexite_lineaire(longueur_max_rouge, k, pas_longueur_rouge,nb_repet)
    courbe_bleue = mesurer_courbe(noms_fonctions[i], longueur_max_bleue, pas_longueur_bleue,nb_repet)


    # Dessiner les trois courbes ensemble en fonction de la taille de luste
    dessine_lignes_brisees(courbe_rouge=courbe_rouge,
                            courbe_bleue=courbe_bleue)

    input("\nAppuyez sur entrée pour continuer.")

    i = i + 1

print("Fin du programme.")
