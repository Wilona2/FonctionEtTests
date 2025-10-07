# Pour chaque fonction une personne différente va :
# a. Programmer la fonction
# b. Créer le plan de tests
# c. Programmer les tests

"""
1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et
les points d'attaques de l'autre et
qui retourne les points de vies restants après l'attaque.
"""

"""
2. Fonction qui reçoit une liste de legos et une couleur et 
qui retourne le pourcentage de blocs de cette couleur
"""

"""
3. Fonction qui reçoit une liste de legos et 
qui retourne il y a combien de blocs de chaque couleur en moyenne
"""

# Répartition des tâches :
"""                     
a   b   c
1   2   3   Nom : Wilona    TODO: c3            
2   3   1   Nom : Maryam                
3   1   2   Nom : Matis               
"""

#a1 (Wilo)
def points(pts_j1: list[int], pts_j2: int) -> int:
    """
    Fonction qui reçoit les points de vies et les points de défenses d'un joueur et
    les points d'attaques de l'autre et qui retourne les points de vies restants après l'attaque.
    :param pts_j1: liste contenant les points de vies et les points de défenses du joueur 1 (ex: pts_j1[pts_vies, pts_def])
    :param pts_j2: points d'attaques du joueur 2
    :return: points de vies restants au premier joueur après l'attaque.
    """
    pts_dmg_j2 = pts_j2 - pts_j1[1]
    pts_restants_j1 = pts_j1[0] - pts_dmg_j2
    return pts_restants_j1

    #



    #(3(a)Matis
    def moyenne_legos(legos: liste) :
        # compteurs couleur
for bloc in legos:
    if bloc == "rouge":
        rouge += 1
    elif bloc == "bleu":
        bleu += 1
    elif bloc == "vert":
        vert += 1
    elif bloc -- "jaune":
        jaune += 1

        # afficher moyenne
        print("Rouge :", nb_rouge)
        print("Bleu:", nb_bleu)
        print("Vert:", nb_vert)
