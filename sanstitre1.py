# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:32:01 2020

@author: Charles
"""
import numpy as np
import matplotlib.pyplot as plt

from parseur_kiro import nb_fournisseurs, matrice_couts
from carte import distance_heuristique

dist=[]

cout_depart=[]
cout_retour=[]

for i in range(nb_fournisseurs):
    dist.append(distance_heuristique(0, i))
    cout_depart.append(matrice_couts[0][i])
    cout_retour.append(matrice_couts[i][0])

dist=np.array(dist)
cout_depart=np.array(cout_depart)
cout_retour=np.array(cout_retour)

plt.plot(dist,cout_depart)
plt.show()


plt.plot(dist,cout_retour)
plt.show()