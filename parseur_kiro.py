# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:19:06 2020
@author: KIRO
"""


##
import numpy as np
import csv as csv
fichier = open("usine.csv", "r", newline = '')
lecture = csv.reader(fichier)
tab = []
for ligne in lecture:
    ligne[0]=ligne[0].split(" ")
    l = []
    for x in ligne[0]:
        if x != '':
            l.append(x)
    tab.append(l)
##

infos_generales = [float(tab[0][1]), int(tab[0][3]), int(tab[0][5])]
Q = int(infos_generales[0])
nb_fournisseurs = infos_generales[1]
horizon = infos_generales[2]


infos_depot = tab[1]
coord_depot = [float(infos_depot[3]), float(infos_depot[4])]


infos_usine = tab[2]
coord_usine = [float(infos_usine[3]), float(infos_usine[4])]
nb_sommets = nb_fournisseurs + 2




infos_fournisseurs_str=tab[3:2+nb_fournisseurs+1]
infos_fournisseurs=[]
for i in range(nb_fournisseurs):
    sous_trait=int(infos_fournisseurs_str[i][3])
    qtes_bibi = []
    for j in range(horizon):
        qtes_bibi.append(int(infos_fournisseurs_str[i][5+j]))
    coord = [float(infos_fournisseurs_str[i][6+horizon]), float(infos_fournisseurs_str[i][7+horizon])]
    fournisseur = [sous_trait, qtes_bibi, coord]
    infos_fournisseurs.append(fournisseur)

    # pour éviter les 10000 variables en auto-complétion
    del sous_trait
    del qtes_bibi
    del coord
    del fournisseur
del infos_fournisseurs_str


# infos_fournisseurs[0] = coût de sous-traitance
# infos_fournisseurs[1] = liste des quantités fournies, par semaine
# infos_fournisseurs[2] = coordonnées sur la carte

##

infos_aretes_str = tab[3+nb_fournisseurs:]
matrice_couts = np.zeros((nb_sommets, nb_sommets))
for el in infos_aretes_str:
    matrice_couts[int(el[1]), int(el[2])] = float(el[4])
del infos_aretes_str



def cout_tournee(tournee):
    """
    cout dune tournee [numero_groupe, semaine, [f1 ,f2 ,f3], [q1 , q2, q3]]
    """
    fournisseurs = tournee[2]
    res = 0
    res += matrice_couts[-2][fournisseurs[0]]
    for i in range(len(fournisseurs) - 1):
        res += matrice_couts[fournisseurs[i]][fournisseurs[i+1]]
    res += matrice_couts[fournisseurs[-1]][-1]
    return res

def cout(sol):
    """
    cout dune solution ie cout de toutes les tournes realisees
    + cout sous_traitance
    """
    res = 0
    x = sol[0]
    y = sol[1]
    for i in range(nb_fournisseurs):
        if x[i]==1:
            res+=infos_fournisseurs[i][0]
    for j in range(len(y)):
        tournee = y[j]
        res+=cout_tournee(tournee)
    return res