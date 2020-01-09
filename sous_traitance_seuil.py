### Calcul des coûts si on ne sous-traite pas

# on commence par calculer le nombre minimal de passages de camions devant être faits pour chaque fournisseur
from math import *
from parseur_kiro import *
nbr_min_passages_camions=[]

for i in range(nb_fournisseurs):
    n=0
    qtes_fournies = infos_fournisseurs[i][1]
    for j in range(horizon):
        bibi_semaine = qtes_fournies[j]
        nb_passages_semaine = ceil(bibi_semaine/Q) # arrondi à l'entier supérieur (module math)
        n+=nb_passages_semaine
    nbr_min_passages_camions.append(n)
    del n
    del nb_passages_semaine
    del bibi_semaine
    del qtes_fournies

def cout_aller_retour(i):
    #cout pour faire depot -> fournisseur i -> usine
    return matrice_couts[nb_fournisseurs][i]+matrice_couts[i][nb_fournisseurs+1]

def cout_min_quand_on_soustraite_pas(i):
    return cout_aller_retour(i)*nbr_min_passages_camions[i]


## sous traités selon un seuil

def sous_traites_avec_seuil(seuil):
    sous_traites = []
    for i in range(nb_fournisseurs):
        if (cout_min_quand_on_soustraite_pas(i)/infos_fournisseurs[i][0]<seuil):
            sous_traites.append(0)
        else:
            sous_traites.append(1)
    return(sous_traites)

