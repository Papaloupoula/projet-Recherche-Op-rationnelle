# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:39:13 2020

@author: OUHAICHI Firas

Calcul des couts si on ne sous-traite pas

on commence par calculer le nombre minimal de passages de camions devant etre faits pour chaque fournisseur

Note pour Killian (si cest toi qui a fait ca) :

    Est que cest pas mieux de changer le calcul de nbr_min_passages_camions
    Pck si le mec il bibi des petites qttes chaque semaine, si ca se trouve
    on peut le caler pour pas tres cher dans la tournee finale dun autre gadjo?

    Du coups jai laisse ton code et jai rajoute un peu du mien :
        au lieu darrondir chaque qtte/Q jarrondis lensemble

    on peut peut-etre aussi faire la moyenne des deux

"""


from math import ceil
from parseur_kiro import nb_fournisseurs, infos_fournisseurs, horizon, matrice_couts, Q
nbr_min_passages_camions=[]

for i in range(nb_fournisseurs):
    n=0
    qtes_fournies = infos_fournisseurs[i][1]
    quant = 0
    for j in range(horizon):
        bibi_semaine = qtes_fournies[j]
        nb_passages_semaine = ceil(bibi_semaine/Q) # arrondi a  l'entier superieur (module math)
        #quant += bibi_semaine
        n+=nb_passages_semaine
    nbr_min_passages_camions.append(n)
    #nbr_min_passages_camions.append(ceil(quant/Q))
    del n
    #del nb_passages_semaine
    del bibi_semaine
    del qtes_fournies

def cout_aller_retour(i):
    """
    cout pour faire depot -> fournisseur i -> usine
    """
    return matrice_couts[nb_fournisseurs][i]+matrice_couts[i][nb_fournisseurs+1]

def cout_min_quand_on_soustraite_pas(i):
    return cout_aller_retour(i)*nbr_min_passages_camions[i]


def sous_traites_avec_seuil(seuil):
    """
    renvoie une liste avec qui est soustraite, selon un certain seuil
    """
    sous_traites = []
    for i in range(nb_fournisseurs):
        if (cout_min_quand_on_soustraite_pas(i)/infos_fournisseurs[i][0]<seuil):
            #quand on ne soustraite pas
            sous_traites.append(0)
        else:
            #on sous traite
            sous_traites.append(1)
    return(sous_traites)

def nbr_de_mec_sous_traite(sous_traite):
    s=0
    for i in range(len(sous_traite)):
        if sous_traite[i]==1:
            s+=1
    return s

sous_traites_bool = sous_traites_avec_seuil(1)
