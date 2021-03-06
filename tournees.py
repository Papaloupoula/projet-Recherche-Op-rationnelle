# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:44:47 2020

@author: OUHAICHI Firas
"""

from parseur_kiro import infos_fournisseurs, horizon, Q
from opti_group import opti_tournee

###Tournée de base groupe
def cree_tournees_groupe(numero,groupe):
    """
    On vide les fournisseurs pour quils aient des demandes inferieurs à Q

    Puis on remplit a la fijas
    """
    tournees_groupe = []
    for s in range(horizon):
        demande=[infos_fournisseurs[i][1][s] for i in groupe]

        for i in range(len(groupe)):
            while demande[i]>Q:
                tournee=[numero,s,[groupe[i]],[Q]]
                tournees_groupe.append(tournee)
                demande[i]=demande[i]-Q

        last_tournees = opti_tournee(groupe, demande, numero, s)
        for t in last_tournees:
            tournees_groupe.append(t)

    return(tournees_groupe)

#def meilleur_jute(numero, groupes):


def cree_tournees(groupes):
    """

    """
    tournees=[]
    for i in range(len(groupes)):
        tournees_groupe = cree_tournees_groupe(i, groupes[i])
        for x in tournees_groupe:
            tournees.append(x)
    return(tournees)