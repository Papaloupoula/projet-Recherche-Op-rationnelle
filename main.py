# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:04:40 2020

@author: Charles
"""
from parseur_kiro import cout
from sousTraitanceSeuil import sous_traites_avec_seuil
#from descente1 import descente1, recuit_simule
from descente2 import descente2, recuit_simule2
from groupes_variation_clusterings import groupes_variation_clustering, n_meilleures_sol

list_seuils = [15]


def main_tarace():
    record = []
    for seuil in list_seuils:
        print("seuil :", seuil)
        sous_traite = sous_traites_avec_seuil(seuil)

        sols_diff_k = groupes_variation_clustering(sous_traite,7,20)

        for i in range(len(sols_diff_k)):
            sols_diff_k[i] = descente2(sols_diff_k[i], 50)

        quatre_meileures_sols = n_meilleures_sol(sols_diff_k,4)

        for i in range(len(quatre_meileures_sols)):
            quatre_meileures_sols[i] = descente2(quatre_meileures_sols[i], 500)

        record.append(n_meilleures_sol(quatre_meileures_sols,1)[0])

    return record

jourgle = main_tarace()

def terminator(sols):
    quatre_meileures_sols = n_meilleures_sol(sols,1)
    for sol in quatre_meileures_sols:
        sol = descente2(sol, 100)


CHARLES = n_meilleures_sol(jourgle,1)[0]
CHARLES = descente2(CHARLES, 100)

#for i in range(20):
#    print(i)
#    cout_o = cout(CHARLES)
#    CHARLES  = recuit_simule2(CHARLES, 100)
#    CHARLES = descente2(CHARLES, 110)


print(cout(CHARLES))

