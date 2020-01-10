# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:27:01 2020

@author: Charles
"""

from parseur_kiro import Q, cout_tournee
import copy as cp

import itertools
g=[5,22,83]
d = [20000,130000,69000]

def opti_tournee(groupe_, demande_, numero_groupe,s):
    """
    optimise les dernieres tournees pour un groupe
    """
    groupe = cp.deepcopy(groupe_)
    demande = cp.deepcopy(demande_)

    m=0
    n=len(groupe)
    tournees_opti=[]
    print("charles")
    #cas on fait des groupes de 1
    for i in range(n):
        tournee = [numero_groupe, s, [groupe[i]], [demande[i]]]
        tournees_opti.append(tournee)
        m+=cout_tournee(tournee)

    tab=[]
    for i in range(n):
        tab.append([groupe[i], demande[i]])

    permuts=list(itertools.permutations(tab))

    #permut avec un groupe de 1 et un groupe restant
    if n>1:

        for permut in permuts:
            tournee1 = [numero_groupe, s, [permut[0][0]], [permut[0][1]]]
            cout=cout_tournee(tournee1)

            quantite=0
            for i in range(1,len(permut)):
                quantite+=permut[i][1]

            if quantite<=Q:
                tournee2=[numero_groupe, s, [permut[i][0] for i in range(1,n)], [permut[i][1] for i in range(1,n)]]
                cout+=cout_tournee(tournee2)
                if cout< m:
                    tournees_opti=[tournee1 , tournee2]
                    m=cout

    #permut avec un groupe de 2 et le reste
    if n==4:
        for permut in permuts:
            quantite1=permut[0][1]+permut[1][1]
            quantite2=permut[2][1]+permut[3][1]
            if quantite1<=Q and quantite2<=Q:
                tournee1 = [numero_groupe, s,[permut[0][0], permut[1][0]], [permut[0][1], permut[1][1]]]
                tournee2 = [numero_groupe, s,[permut[2][0], permut[3][0]], [permut[2][1], permut[3][1]]]
                cout= cout_tournee(tournee1) + cout_tournee(tournee2)
                if cout<m:
                    tournees_opti=[tournee1 , tournee2]
                    m=cout
    #tous ensembles
    for permut in permuts:
        quantite = 0
        for i in range(n):
            quantite+= permut[i][1]
        if quantite <= Q:
            tournee=[numero_groupe, s, [permut[i][0] for i in range(n)], [permut[i][1] for i in range(n)]]
            cout = cout_tournee(tournee)
            if cout<m:
                tournees_opti=[tournee]

    #Autre remplissage
    #a laisser a la fin car modifie demande

    #ERREUR FIRAS SE DEMERDE

    for permut in permuts:
        tour=[]
        cout=0
        for i in range(n):
            quantite_tot=0
            quant_fournisseur=[]
            fournisseur_livre=[]
            for j in range(i,n):
                if permut[j][1]>0:
                    if quantite_tot<Q:
                        on_prend=min(Q-quantite_tot,permut[j][1])
                        quant_fournisseur.append(on_prend)
                        fournisseur_livre.append(permut[j][0])
                        quantite_tot+=on_prend
                        permut[j][1]=permut[j][1]-on_prend
            if len(fournisseur_livre)>0:
                tournee=[numero_groupe, s, fournisseur_livre, quant_fournisseur]
                cout+=cout_tournee(tournee)
                tour.append(tournee)

        if cout<m and len(tour)>0:
            m=cout
            tournees_opti=tour


    return tournees_opti

def opti_vidage(groupe_, demande_, numero_groupe, s):
    demande=cp.deepcopy(demande_)
    groupe=cp.deepcopy(groupe_)
    
    #Vidage simple
    vidage_opti=[]
    tournee=[]
    m=0
    for i in range(len(groupe)):
        while demande[i]>Q:
            tournee=[numero_groupe,s,[groupe[i]],[Q]]
            vidage_opti.append(tournee)
            m+=cout_tournee(tournee)
            demande[i]=demande[i]-Q
    
    #Optimisation
    groupe_rempli=[]
    for i in range(len(groupe)):
        groupe_rempli.append([groupe_[i],demande_[i]//Q])
    permuts=list(itertools.permutations(groupe_rempli))
    for permut in permuts:
        vidage=[]
        cout=0
        iteration=0
        n=nb_rempli(permut, iteration)
        while n>0:
            if n==3:
                for el in permut:
                    if el[1]>iteration:
                        tournee=[numero_groupe,s,[el[0]],Q]
                        vidage.append(tournee)
                        cout+=cout_tournee(tournee)
            else:
                quant=[]
                fournisseur=[]
                quantite=Q/n
                for el in permut:
                    if el[1]>iteration:
                        quant.append(quantite)
                        fournisseur.append(el[0])
                tournee=[numero_groupe, s, fournisseur, quant]
                for i in range(n):
                    vidage.append(tournee)
                    cout+=cout_tournee(tournee)
            iteration+=1
            n=nb_rempli(permut,iteration)
        if cout<m:
            vidage_opti=vidage
            m=cout
    return vidage_opti
    
def nb_rempli(tableau, iteration):
    rempli=0
    for element in tableau:
        if element[1]-iteration>0:
            rempli+=1
    return rempli



