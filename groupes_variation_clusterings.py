# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:39:13 2020

@author: OUHAICHI Firas
"""

from kmeans import correspondance
from parseur_kiro import cout
from constitution_groupe import constit_groupe_simple, isolement
from tournees import cree_tournees
from sousTraitanceSeuil import sous_traites_avec_seuil

from sklearn.cluster import KMeans


def groupes_variation_clustering(sous_traites,a,b):
    """
    groupes en faisant varier les clusterings
    """
    solutions=[]
    for i in range(a,b):

        corresp, x = correspondance(sous_traites)

        kmeans = KMeans(i)
        kmeans.fit(x)
        clustos=kmeans.labels_

        groupe0 = constit_groupe_simple(isolement(clustos, i, corresp))

        tournees0 = cree_tournees(groupe0)

        solution0 = [sous_traites, tournees0, groupe0]

        solutions.append(solution0)
    return(solutions)

def n_meilleures_sol(solutions, N):
    """
    donne les N meilleures solutions
    """
    couts_solution=[]
    for x in solutions:
        couts_solution.append(cout(x))

    indice_min = 0
    N_meilleurs = []
    couts_N_meilleurs = []
    for j in range(N):
        cout_sol = 10000000000000
        for i in range(len(couts_solution)):
            if couts_solution[i] < cout_sol and (i not in N_meilleurs):
                cout_sol = couts_solution[i]
                indice_min = i
        N_meilleurs.append(indice_min)
        couts_N_meilleurs.append(cout_sol)

    print(N_meilleurs)
    return [solutions[i] for i in N_meilleurs]

##

solutions = groupes_variation_clustering(sous_traites_avec_seuil(1),19,20)
meilleure_sol_originale = n_meilleures_sol(solutions, 1)[0]