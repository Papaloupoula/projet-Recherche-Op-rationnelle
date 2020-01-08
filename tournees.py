# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:44:47 2020

@author: OUHAICHI Firas
"""

from parseur_kiro import *
from constitution_groupe import *
from fct_cout import *
from opti_group import *

tournees=[]
###Tournée de base groupe
def tournee_les_serviettes(numero_groupe,groupe):
    """
    groupe=[f1,f2,f3,f4] si il y a 4 fournisseurs pex
    """
    t=[]
    for s in range(horizon):
        demande=[infos_fournisseurs[i][1][s] for i in groupe]

        for i in range(len(groupe)):
            #On vide les fournisseurs pour qu'ils aient des demandes inférieurs à Q
            while demande[i]>Q:
                tournee=[numero_groupe,s,[groupe[i]],[Q]]
                t.append(tournee)
                demande[i]=demande[i]-Q

        tournees_finales=opti_tournee(groupe, demande, numero_groupe,s)
        for tournee in tournees_finales:
            t.append(tournee)
    return t



#            for j in range(i,len(groupe)):
#                if demande[j]>0:
#                    if quantite_tot<Q:
#                        on_prend=min(Q-quantite_tot,demande[j])
#                        quant_fournisseur.append(on_prend)
#                        fournisseur_livre.append(groupe[j])
#                        quantite_tot+=on_prend
#                        demande[j]=demande[j]-on_prend
#            if len(fournisseur_livre)>0:
#                tournee=[numero_groupe,s,fournisseur_livre,quant_fournisseur]
#                tournees.append(tournee)


tournees=[]
for i in range(len(GROUP)):
    print(i)
    G=GROUP[i]
    tournees_group = tournee_les_serviettes(i,G)

    for tournee in tournees_group:
        tournees.append(tournee)

solution=[sous_traites_bool,tournees,GROUP]
print(cout(solution))

