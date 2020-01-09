# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:39:13 2020

@author: Bakong Killian
"""

## Fonction coût
from parseur_kiro import *
"""
soit une solution sol=[x, y, z]
x = liste des fournisseurs, 1 s'ils sont sous-traités, 0 sinon
y = tournées
z = groupes
"""

##
def cout_tournee(tournee):
    fournisseurs = tournee[2]
    res = 0
    res += matrice_couts[-2][fournisseurs[0]]
    for i in range(len(fournisseurs) - 1):
        res += matrice_couts[fournisseurs[i]][fournisseurs[i+1]]
    res += matrice_couts[fournisseurs[-1]][-1]
    return res

def cout(sol):
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

