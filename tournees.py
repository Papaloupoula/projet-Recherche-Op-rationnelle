# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:44:47 2020

@author: OUHAICHI Firas
"""

from parseur_kiro import *
from groupe import *
from fct_cout import *
tournees=[]
###Tournée de base groupe
def tournee(numero,groupe):
    #On vide les fournisseurs pour qu'ils aient des demandes inférieurs à Q
    for s in range(horizon):
        demande=[infos_fournisseurs[i][1][s] for i in groupe]
        for i in range(len(groupe)):
            while demande[i]>Q:
                tournee=[numero,s,[groupe[i]],[Q]]
                tournees.append(tournee)
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
                tournees.append(tournee)

for i in range(len(GROUP)):
    tournee(i,GROUP[i])

solution=[[False for i in range(nb_fournisseurs) ],tournees,GROUP] 
print(cout(solution))                 
                
                