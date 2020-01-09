# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:04:40 2020

@author: Charles
"""
from parseur_kiro import cout
from sousTraitanceSeuil import sous_traites_avec_seuil
from kmeans import correspondance
from descente1 import descente1
from groupes_variation_clusterings import groupes_variation_clustering, n_meilleures_sol

list_seuils = [1, 1.5, 2, 3, 4, 5, 7.5, 10, 12.5, 15, 20, 30]


def main_tarace():
    record = []
    for seuil in list_seuils:
        print("seuil :", seuil)
        sous_traite = sous_traites_avec_seuil(seuil)

        sols_diff_k = groupes_variation_clustering(10, sous_traite)

        quatre_meileures_sols = n_meilleures_sol(sols_diff_k,3)

        for sol in quatre_meileures_sols:
            descente1(sol, 150)

        record.append(n_meilleures_sol(quatre_meileures_sols,1)[0])

    return record

jourgle = main_tarace()

def terminator(sols):
    quatre_meileures_sols = n_meilleures_sol(sols,1)
    for sol in quatre_meileures_sols:
        descente1(sol, 1000)

terminator(jourgle)

CHARLES = n_meilleures_sol(jourgle,1)[0]
descente1(jourgle[CHARLES], 1000)
