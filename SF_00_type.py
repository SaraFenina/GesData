"""
    Auteur:" Sara Fenina "
    Crée le 07/03/2025
    PARTIE 1 : semaine 1
    contient : Nouveau type :Formation
               fonction affiche-Formation
"""

from dataclasses import dataclass

#Déclarer un nouveau type de donnée : les données "Formation" correspendent au formations des apprentis dans le domaine social et sanitaire 
@dataclass
class Formation:
    domaine : str
    formation : str
    niveau : int

    
#Une fonction qui permet d'afficher les instances du type de donnée "Formation" nouvellement crée 
def affiche_Formation(forma):
    """
Rôle : affiche les informations de forma
Type de la donnée : forma : Formation
    """
    print("\nLe domaine de l'apprentis est dans le",forma.domaine)
    print("La formation de l'apprantis est",forma.formation)
    print("Le niveau de fomation de l'apprantis est",forma.niveau)

    

