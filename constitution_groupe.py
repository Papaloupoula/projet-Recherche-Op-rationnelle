# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:19:06 2020
@author: OUHAICHI Firas
"""

def isolement(clustre,n_clustre, corresp):
    """
    renvoies un liste avec en ieme entree la liste des fournisseurs
    du cluster i
    """
    fournisseurs_groupes=[]
    for i in range(n_clustre):
        fournisseurs_groupes.append([])

    for i in range(len(clustre)):
        fournisseurs_groupes[clustre[i]].append(corresp[i])

    return fournisseurs_groupes

def constit_groupe_simple(fournisseurs_groupes):
    """
    constitue des groupes simplement avec le cluster
    """
    groupes=[]
    a=-1
    for i in range(len(fournisseurs_groupes)):
        for j in range(len(fournisseurs_groupes[i])):
            if len(groupes)==0 or len(groupes[a])>=4:
                a+=1
                groupes.append([fournisseurs_groupes[i][j]])
            else:
                groupes[a].append(fournisseurs_groupes[i][j])
    return groupes

