"""
    Auteur : Sara Fenina
    Crée le 07/03/2025
    PARTIE 1 : Semaine 1
    Contient : fonction affiche_liste_Formation
                        transformation_chaine_forma
                        maximum_niveau
                        minimum_niveau
                        moyenne_niveau
                        ecart_type_niveau
                        filtrer
    PARTIE 2 : Semaine 2
    Contient : fonction nombre_occurrences_niveau
                        recherche_grand_niveau
                        recherche_petit_niveau
                        recherche_dicho_niveau
                        est_triee
                        tri_selection
                        mediane_niveau
                        modalites_niveau
                        
"""

from SF_00_type import*


#PARTIE 1




#Fonction qui affiche les donnée d'une liste 
def affiche_liste_Formation(lforma) :
    """
Rôle : affiche la liste des informations des formations
Type des données :
    lforma : liste de valeurs de type Fomation
    
    """
    if len(lforma)==0:
        print("Aucune Formation")
    else:
        for i in range (0,len(lforma)):
            affiche_Formation(lforma[i])
        
    





# Fonction qui transforme une liste de listes de chaînes de caractères en une liste d'instances du type Formation
def transformation_chaine_forma(liste_donnees, lforma):
    """
    Rôle: Transforme une liste de listes de chaînes de caractères en une liste d'instances du type Formation.
    Type des données :
        liste_donnees : liste de listes de chaînes de caractères.
        lforma : liste de valeurs type Formation
    Type de Résultats : liste de valeur de Formation
    """

    for i in range(len(liste_donnees)):
        ligne = liste_donnees[i]
        if ligne != "":

            if len(ligne) >= 18:
                domaine = ligne[0]
                formation = ligne[15]
                niveau = None  # Niveau vide par défaut

                if ligne[18] != "":
                    valeur = int(ligne[18])
                    if 2 < valeur < 8:
                        niveau = valeur
                if niveau is not None:
                    lforma.append(Formation(domaine, formation, niveau))

                
                
    return lforma





def maximum_niveau(lforma):
    """
    Rôle : Cherche le maximum de la valeur numérique du type Formation
    Précondition : la liste lforma contient au moins un élément.
    Type de données :
        lforma : liste de valeurs de type Formation
    Type de Résultat : nombre
    """
    maximum = lforma[0].niveau
    for i in range(1, len(lforma)):
        if lforma[i].niveau > maximum:
            maximum = lforma[i].niveau
    return maximum



def minimum_niveau(lforma):
    """
    Rôle : Cherche le minimum de la valeur numérique du type Formation
    Précondition : la liste lforma n'est pas vide
    Type de données :
        lforma : liste de valeurs de type Formation
    Type de Résultat : nombre
    """
    minimum = lforma[0].niveau
    for i in range(1, len(lforma)):
        if lforma[i].niveau < minimum:
            minimum = lforma[i].niveau
    return minimum


def moyenne_niveau(lforma):
    """
    Rôle : Calcule la moyenne des éléments de lforma
    Précondition : la liste lforma n'est pas vide
    Données :
        lforma : Liste de valeurs de type Formation
    Type de Résultat : float
    """
    longueur = len(lforma)
    somme = 0
    for i in range(longueur):
        somme = somme + lforma[i].niveau

    moyenne = somme / longueur
    return moyenne



def ecart_type_niveau(lforma):
    """
    Rôle : Calcule l’écart-type des éléments de lforma
    Précondition : la liste lforma n'est pas vide
    Données :
        lforma : Liste de valeurs de type Formation
    Type de Résultat : float
    """
    longueur = len(lforma)
    moyenne = moyenne_niveau(lforma)
    somme_ecart = 0
    for i in range(longueur):
        somme_ecart = somme_ecart + (lforma[i].niveau - moyenne) ** 2

    ecart = (somme_ecart / longueur) ** 0.5
    return ecart





def filtrer(lforma, critere):
    """
    Rôle : Filtrer l'affichage des valeurs de lforma en fonction du critère donné.
    Données:
        lforma : Liste de valeurs de type Formation
        critere : Chaîne de caractères
    Résultat : Liste de valeurs Formation correspondant au critère
    """
    liste_affiche = []
    for i in range(len(lforma)):
        
        if critere == lforma[i].domaine or critere == lforma[i].formation:
            liste_affiche.append(lforma[i])

    return liste_affiche





#PARTIE 2

def est_triee(lforma):
    """
    Rôle : Vérifie si la liste est triée par ordre croissant selon le champ numérique `niveau`.
    Données :
        lforma : liste de formations.
    Résultat :
        booléen 
    """
    i = 0
    est_bien_triee = True
    while i < len(lforma) - 1:
        if lforma[i].niveau > lforma[i + 1].niveau:
            est_bien_triee = False
        i = i + 1
    return est_bien_triee


def tri_selection(lforma):
    """
    Rôle : Trie la liste par ordre croissant selon le champ numérique 'niveau',
           en utilisant l'algorithme du tri par sélection.
    Données :
        lforma : liste de formations
        indice_min : entier
        temp : entier
   
    """
    longeur = len(lforma)
    for i in range(longeur - 1):
        
        indice_min = i
        for j in range(i + 1, longeur):
            if lforma[j].niveau < lforma[indice_min].niveau:
                indice_min = j
 
        temp = lforma[i]
        lforma[i] = lforma[indice_min]
        lforma[indice_min] = temp


def mediane_niveau(lforma):
    """
    Rôle : caluler la mediane des niveau dans  le type formation
    Type de donéee :
        lforma : liste de valeur de type Formation
     Prédondition :
             lforma non vide
    type de resultat :
        mediane : float
    """
    
    longueur = len(lforma)
    mediane = 0  


    if longueur % 2 == 1: #si pair 
        mediane = lforma[longueur // 2].niveau
    else:  #si impaire 
        mediane = (lforma[(longueur // 2) - 1].niveau + lforma[longueur // 2].niveau) / 2

    return mediane


def modalites_niveau(lforma):
    """
    Rôle : calculer les modalité du champ numerique triée de Formation
    Type de donnee:
        lforma : liste de valeur de type Formation
        Prédondition :
             liste lforma a ses valeur niveau triée
    Type de resultat :
         modalites : liste
    """
    
    modalites = []

    if len(lforma) > 0:
        modalites.append(lforma[0].niveau)  

        for i in range(1, len(lforma)):
            if lforma[i].niveau != lforma[i - 1].niveau:
                modalites.append(lforma[i].niveau)

    return modalites


def recherche_dicho_niveau(lforma, valeur):
    """
    Rôle :Recherche dichotomique dans une liste triée selon le niveau des formation.

    Type de Données :
        lforma : liste d'objets de type Formation
        valeur : nombre

        Précondition : lforma triée

    Resulats :
        nombre
    """
    if len(lforma)==0:
        indice_occurance = -1
        
    gauche = 0
    droite = len(lforma) - 1
    indice_occurance = -1

    while ( gauche <= droite ) and( indice_occurance== -1 ):
        milieu = (gauche + droite) // 2

        if lforma[milieu].niveau == valeur:
            indice_occurance = milieu
  
            
        elif lforma[milieu].niveau < valeur:
            gauche = milieu + 1
            
        else:
            droite = milieu - 1

    return indice_occurance

    
def recherche_petit_niveau(lforma, valeur):
    """
    Rôle : Recherche dichotomique du plus petit indice dans une liste triée selon le niveau des formations.
    Type de Données :
        lforma : liste d'objets de type Formation
        valeur : nombre
    Précondition : lforma triée
    Résultat :
        nombre
    """
    gauche = 0
    droite = len(lforma) - 1
    indice_min_occurance = -1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        if lforma[milieu].niveau == valeur:
            indice_min_occurance = milieu
            droite = milieu - 1 

        elif lforma[milieu].niveau < valeur:
            gauche = milieu + 1
            
        else:
            droite = milieu - 1

    return indice_min_occurance





def recherche_grand_niveau(lforma, valeur):
    """
    Rôle :Recherche dichotomique du plus grand indice dans une liste triée selon le niveau des formation.

    Type de Données :
        lforma : liste d'objets de type Formation
        valeur : nombre

        Précondition : lforma triée

    Resulats :
        nombre
    """

    gauche = 0
    droite = len(lforma) - 1
    indice_max_occurance = -1

    while ( gauche <= droite ) :
        milieu = (gauche + droite) // 2

        if lforma[milieu].niveau == valeur:
            indice_max_occurance = milieu
            gauche= milieu + 1
  
            
        elif lforma[milieu].niveau < valeur:
            gauche = milieu + 1
            
        else:
            droite = milieu - 1

    return indice_max_occurance


def nombre_occurrences_niveau(lforma, valeur):
    """
    Rôle :Retourne le nombre d'occurrences des niveau dans une liste Fromation
    
    Type de Données :
         lforma : liste d'objets de type Formation
        valeur : nombre
        
    Resultat:
        nombre
    """
    premier = recherche_petit_niveau(lforma, valeur)
    dernier = recherche_grand_niveau(lforma, valeur)

    if premier == -1:
        nb_occurrences = 0
    else:
        nb_occurrences = dernier - premier + 1

    return nb_occurrences



    
