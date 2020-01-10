## parseur de solutions
import numpy as np
import csv as csv

def reparseur(str_fichier):
    fichier = open("solution.csv", "r", newline = '')
    lecture = csv.reader(fichier)
    tab = []
    for ligne in lecture:
        ligne[0]=ligne[0].split(" ")
        l = []
        for x in ligne[0]:
            if x != '':
                l.append(x)
        tab.append(l)
    
    
    infos_sous_traitance = tab[0]
    nb_sous_trait = int(infos_sous_traitance[1])
    sous_traites_ind = [int(infos_sous_traitance[i]) for i in range(3, 3 + nb_sous_trait)]
    sous_traites_bool0 = [0 for i in range(nb_fournisseurs)]
    for i in range(nb_sous_trait):
        sous_traites_bool0[sous_traites_ind[i]] = 1
    
    
    nb_tournees = int(tab[1][1])
    nb_groupes = int(tab[2][1])
    
    groupes_str = []
    for i in range(3, 3 + nb_groupes):
        groupes_str.append(tab[i])
    
    groupes0=[]
    for x in groupes_str:
        groupes0.append([])
        nb_el_ds_grp = int(x[3])
        for i in range(5, 5+nb_el_ds_grp):
            groupes0[-1].append(int(x[i]))
    
    
    tournees_str = []
    for i in range(3 + nb_groupes, len(tab)):
        tournees_str.append(tab[i])
    
    tournees0=[]
    for x in tournees_str:
        groupe_tournee = int(x[3])
        semaine_tournee = int(x[5])
        nb_fourn_tournee = int(x[7])
        fourns_tournee = []
        qtes_tournee = []
        for i in range(8, 8 + 3*nb_fourn_tournee):
            if i%3 == 0:
                fourns_tournee.append(int(x[i]))
            if i%3 == 1:
                qtes_tournee.append(int(x[i]))
        tournee = [groupe_tournee, semaine_tournee, fourns_tournee, qtes_tournee]
        tournees0.append(tournee)
    
    solution0 = [sous_traites_bool0, tournees0, groupes0]
    return(solution0)