# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:19:06 2020
@author: BAK
"""


import random as rd
import copy as cp

import math as m

from parseur_kiro import nb_fournisseurs, cout
from tournees import cree_tournees


## Échange de deux fournisseurs

def echange_fournisseurs(fourn1, fourn2, sous_traites0, groupes_ech):
    """
    échange deux fournisseurs pour une liste de sous-traitance
    et une liste de groupes_ech données
    modifie la liste de sous-traitance et celle des groupes_ech
    """

    assert(fourn1 != fourn2)

    fourn1_est_soustraite = sous_traites0[fourn1]
    fourn2_est_soustraite = sous_traites0[fourn2]
    #print("st f1", fourn1_est_soustraite)
    #print("st f2", fourn2_est_soustraite)
    indice_groupe_f1 = -1
    indice_groupe_f2 = -1

    for j in range(len(groupes_ech)):
        groupe_en_cours = groupes_ech[j]
        if fourn1 in groupe_en_cours:
            indice_groupe_f1 = j
        if fourn2 in groupe_en_cours:
            indice_groupe_f2 = j
    #print("grp1", indice_groupe_f1)
    #print("grp2", indice_groupe_f2)

    #"0e cas" les deux sont sous traites, on ne fait rien
    if fourn1_est_soustraite == 1 and fourn2_est_soustraite == 1:
        on_est_al = 1

    # 1er cas: l'un des deux est sous-traité
    elif fourn1_est_soustraite == 1 and fourn2_est_soustraite == 0:
        #maintenant, on échange les rôles des deux fournisseurs
        # on sous-traite le 2
        sous_traites0[fourn1] = 0
        sous_traites0[fourn2] = 1

        # on trouve le groupe du 2 et on met le 1 à la place
        groupe_f2 = groupes_ech[indice_groupe_f2]
        for k in range(len(groupe_f2)):
            if groupe_f2[k] == fourn2:
                del groupe_f2[k]
                groupe_f2.append(fourn1)

    elif fourn2_est_soustraite == 1 and fourn1_est_soustraite == 0:
        sous_traites0[fourn1] = 1
        sous_traites0[fourn2] = 0

        # on trouve le groupe du 1 et on met le 2 à la place
        groupe_f1 = groupes_ech[indice_groupe_f1]
        for k in range(len(groupe_f1)):
            if groupe_f1[k] == fourn1:
                del groupe_f1[k]
                groupe_f1.append(fourn2)

    # 2d cas : aucun des deux n'est sous-traité
    else:
        groupe_f1 = groupes_ech[indice_groupe_f1]
        groupe_f2 = groupes_ech[indice_groupe_f2]
        for k in range(len(groupe_f1)):
            if groupe_f1[k] == fourn1:
                del groupe_f1[k]
                groupe_f1.append(fourn2)
        for k in range(len(groupe_f2)):
            if groupe_f2[k] == fourn2:
                del groupe_f2[k]
                groupe_f2.append(fourn1)

    #print("xxxxxxxxxxxxxxxx")
    #print("f1:", fourn1)
    #print("f2:", fourn2)
    #fourn1_est_soustraite = sous_traites0[fourn1]
    #fourn2_est_soustraite = sous_traites0[fourn2]
    #print("st f1", fourn1_est_soustraite)
    #print("st f2", fourn2_est_soustraite)
#    indice_groupe_f1 = -1
#    indice_groupe_f2 = -1
#    for j in range(len(groupes_ech)):
#        groupe_en_cours = groupes_ech[j]
#        if fourn1 in groupe_en_cours:
#            indice_groupe_f1 = j
#        if fourn2 in groupe_en_cours:
#            indice_groupe_f2 = j
    #print("grp1", indice_groupe_f1)
    #print("grp2", indice_groupe_f2)
    #print("XXXXXXXXXXXXXXXXX")
    #print("XXXXXXXXXXXXXXXXX")

## Descente de gradient


def descente1(solution_originale, iterations_max):
    i=0
    solution_en_cours = cp.deepcopy(solution_originale)
    while i < iterations_max:
        sous_traites0 = cp.deepcopy(solution_en_cours[0])
        groupes_desc = cp.deepcopy(solution_en_cours[2])
        cout_sol = cout(solution_en_cours)

        # on commence par générer deux fournisseurs à échanger aléatoirement
        fournisseur1 = rd.randint(0, nb_fournisseurs-1)
        fournisseur2 = rd.randint(0, nb_fournisseurs-1)

        while fournisseur1 == fournisseur2:
            fournisseur2 = rd.randint(0, nb_fournisseurs-1)

        # while fournisseur1 == fournisseur2 or (fournisseur1_est_soustraite == 1 and fournisseur2_est_soustraite ==  1) or (indice_groupe_f1 == indice_groupe_f2):
        #     fournisseur2 = rd.randint(0, nb_fournisseurs)

        # on échange les fournisseurs grâce à la fonction auxiliaire
        echange_fournisseurs(fournisseur1, fournisseur2, sous_traites0, groupes_desc)

        # maintenant qu'on a un nouveau groupe, on en génère les tournées
        tournees_desc = cree_tournees(groupes_desc)

        # on a maintenant une nouvelle solution, qu'on garde si elle est meilleure
        nv_solution = [sous_traites0, tournees_desc, groupes_desc]
        nv_cout = cout(nv_solution)

        #print("nv_cout :", nv_cout)
        #print("cout_ori :", cout_sol)
        if nv_cout <= cout_sol:
            solution_en_cours = cp.deepcopy(nv_solution)
            #print(nv_cout)

        #print(i)
        i+=1
    return(solution_en_cours)


def recuit_simule(solution_originale, iterations_max):
    """
    faire avec 100
    """
    beta = 150000
    i=0
    solution_en_cours = cp.deepcopy(solution_originale)
    while i < iterations_max:
        sous_traites0 = cp.deepcopy(solution_en_cours[0])
        groupes_desc = cp.deepcopy(solution_en_cours[2])
        cout_sol = cout(solution_en_cours)

        # on commence par générer deux fournisseurs à échanger aléatoirement
        fournisseur1 = rd.randint(0, nb_fournisseurs-1)
        fournisseur2 = rd.randint(0, nb_fournisseurs-1)

        while fournisseur1 == fournisseur2:
            fournisseur2 = rd.randint(0, nb_fournisseurs-1)

        # while fournisseur1 == fournisseur2 or (fournisseur1_est_soustraite == 1 and fournisseur2_est_soustraite ==  1) or (indice_groupe_f1 == indice_groupe_f2):
        #     fournisseur2 = rd.randint(0, nb_fournisseurs)

        # on échange les fournisseurs grâce à la fonction auxiliaire
        echange_fournisseurs(fournisseur1, fournisseur2, sous_traites0, groupes_desc)

        # maintenant qu'on a un nouveau groupe, on en génère les tournées
        tournees_desc = cree_tournees(groupes_desc)

        # on a maintenant une nouvelle solution, qu'on garde si elle est meilleure
        nv_solution = [sous_traites0, tournees_desc, groupes_desc]
        nv_cout = cout(nv_solution)

        if nv_cout <= cout_sol:
            solution_en_cours = cp.deepcopy(nv_solution)
            #print(nv_cout)

        #la partie quon rajoute pour le recuit simule
        else :
            T = 10*(iterations_max - i)/iterations_max
            energie = nv_cout - cout_sol
            proba = m.exp(-energie/(beta*T))
            p = rd.random()
            if p <= proba:
                solution_en_cours = nv_solution
        i+=1

    return(solution_en_cours)

