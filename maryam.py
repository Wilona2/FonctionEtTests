#2. Fonction qui reçoit une liste de legos et une couleur et qui retourne le pourcentage de blocs de cette couleur
# a. Programmer la fonction

def liste_legos(couleurs, pourcentages_blocs) -> int:
    """
    la fonctions qui recois la liste de legos et sa couleurs avec son pourcenatge de la couleur
    :param couleurs: La couleur assigner au bloc de couleur
    :param pourcentages_blocs: Le pourcentage de couleurs dans un bloc de lego
    :return: le bloc de lego obtenu
    """
    lego = couleurs + pourcentages_blocs
    return lego


## b. Créer le plan de tests
"""
3. Fonction qui reçoit une liste de legos et 
qui retourne il y a combien de blocs de chaque couleur en moyenne
"""

import pytest




