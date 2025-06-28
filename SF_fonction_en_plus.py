"""
    Auteur : Sara Fenina
    Crée le 21/03/2025
    PARTIE 1 :Semaine 3
    Contient : Fonction verif_critere
                        verif_choix
                        affiche_statistiques
                        
                        
"""

from SF_02_listes_type import *


def affiche_statistiques(lforma):
    """
    Rôle : Affichage du nombre d'enregistrements, minimum, maximum, moyenne et écart-type.
    Type de Données :
        lforma = Liste de valeurs de Formation.
        Précondition : lfroma n'est pas vide
    """
    
    print("-----------------")
    print("Ci-suit les statistiques des niveaux de formation du fichier choisi ")
    minimum=minimum_niveau(lforma)
    maximum=maximum_niveau(lforma)
    moyenne=moyenne_niveau(lforma)
    ecart=ecart_type_niveau(lforma)
    mediane = mediane_niveau(lforma)

    modalites = modalites_niveau(lforma)
    print("Les modalités des niveaux de formation sont : ", modalites)
    print("Le nombre d'enregistrements est", len(lforma))
    print("Le niveau maximum des formations est : ",maximum)
    print("Le niveau minimum des formations est : ",minimum)
    print("La moyenne des niveau est ",moyenne)
    print("L'ecart type des niveau de formation est ",ecart)
    print("La mediane des niveau de formation est ",mediane)
    


def verif_critere(critere):
    """
    Rôle: Vérifie si le critère est valide et contient uniquement des caractères alphabétiques et des caractères spéciaux acceptés
    Type de Données :
        critere: un champ non numérique qui sert de critère au filtre
    Type de Résultat: Booléen
    """

    lettre_acceptee = ["À", "Â", "É", "È", "Ê", "à", "á", "â", "æ", "ç", "è", "é", "ê", "ì", "í", "î", "œ", "-", "_"]
    i = 0
    est_valide = True
    
    while i < len(critere) and est_valide:
        caractere = critere[i]
        if not (("a" <= caractere <= "z") or ("A" <= caractere <= "Z") or caractere == " "):
            j = 0
            lettre_acceptee_trouvee = False
            while j < len(lettre_acceptee) and not lettre_acceptee_trouvee:
                if caractere == lettre_acceptee[j]:
                    lettre_acceptee_trouvee = True
                j=j+1

            if not lettre_acceptee_trouvee:
                est_valide = False
        
        i=i+1

    return est_valide



def verif_choix(choix_fichier, taille_liste):
    """
    Rôle: Vérifie si le choix de l'utilisateur est un nombre valide et dans la plage des indices.
    
    Type de Données :
        choix_fichier : str : L'indice donné par l'utilisateur sous forme de chaîne.
        taille_liste : int : La taille de la liste de fichiers disponibles.
    
    Type de Resulats:Booleen
    """

    est_valide = False
    
    if 1 <= int(choix_fichier) <= taille_liste:
        est_valide = True  
    
    return est_valide






