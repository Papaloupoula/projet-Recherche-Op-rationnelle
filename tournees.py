# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:44:47 2020

@author: OUHAICHI Firas
"""

from parseur_kiro import infos_fournisseurs, horizon, Q

###Tournée de base groupe
def cree_tournees_groupe(numero,groupe):
    """
    On vide les fournisseurs pour quils aient des demandes inférieurs à Q
    """
    tournees_groupe = []
    for s in range(horizon):
        demande=[infos_fournisseurs[i][1][s] for i in groupe]
        for i in range(len(groupe)):
            while demande[i]>Q:
                tournee=[numero,s,[groupe[i]],[Q]]
                tournees_groupe.append(tournee)
                demande[i]=demande[i]-Q
        for i in range(len(groupe)):
            quantite_tot=0
            quant_fournisseur=[]
            fournisseur_livre=[]
            for j in range(i,len(groupe)):
                if demande[j]>0:
                    if quantite_tot<Q:
                        on_prend=min(Q-quantite_tot,demande[j])
                        quant_fournisseur.append(on_prend)
                        fournisseur_livre.append(groupe[j])
                        quantite_tot+=on_prend
                        demande[j]=demande[j]-on_prend
            if len(fournisseur_livre)>0:
                tournee=[numero,s,fournisseur_livre,quant_fournisseur]
                tournees_groupe.append(tournee)
    return(tournees_groupe)


def cree_tournees(groupes):
    """

    """
    tournees=[]
    for i in range(len(groupes)):
        tournees_groupe = cree_tournees_groupe(i, groupes[i])
        for x in tournees_groupe:
            tournees.append(x)
    return(tournees)