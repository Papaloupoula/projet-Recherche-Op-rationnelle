# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:39:13 2020

@author: OUHAICHI Firas
"""
#on importe les bibliotheques

n_clusters = 10

import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

from parseur_kiro import infos_fournisseurs
from sous_traitance_seuil import sous_traites_bool


def correspondance(sous_traites):
    """

    """

    x0=[]
    corresp0=[]
    for i in range(len(infos_fournisseurs)):
        if sous_traites[i]==0:
            x0.append([infos_fournisseurs[i][2][0],infos_fournisseurs[i][2][1]])
            corresp0.append(i)
    x0=np.array(x0)
    return(corresp0, x0)

x=correspondance(sous_traites_bool)[1]

plt.scatter(x[:,0],x[:,1], label='True Position')

kmeans = KMeans(n_clusters)
kmeans.fit(x)

clust0=kmeans.labels_
plt.scatter(x[:,0],x[:,1], c=kmeans.labels_, cmap='rainbow')
