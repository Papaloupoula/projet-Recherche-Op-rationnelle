# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:47:07 2020

@author: Charles
"""
#on importe les bibliotheques

n_clusters = 10

import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

from solution_triviale import sous_traites_bool

#on importe les donnees

from parseur_kiro import infos_fournisseurs
x=[]
for i in range(len(infos_fournisseurs)):
    #if sous_traites_bool[i]==0:
        x.append([infos_fournisseurs[i][2][0],infos_fournisseurs[i][2][1]])

x=np.array(x)

plt.scatter(x[:,0],x[:,1], label='True Position')

kmeans = KMeans(n_clusters)
kmeans.fit(x)

print(kmeans.cluster_centers_)

print(kmeans.labels_)

plt.scatter(x[:,0],x[:,1], c=kmeans.labels_, cmap='rainbow')