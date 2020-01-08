from sklearn.cluster import MiniBatchKMeans
def distance_heuristique(i, j): #renvoie la distance à vol d'oiseau entre deux fournisseurs i et j
    dist = (infos_fournisseurs[i][2][0] - infos_fournisseurs[j][2][0])**2 + (infos_fournisseurs[i][2][1] - infos_fournisseurs[j][2][1])**2
    return(dist)

import matplotlib.pyplot as plt

abs=[]
ord=[]
n = [i for i in range(i)]
for i in range(nb_fournisseurs):
    abs.append(infos_fournisseurs[i][2][0])
    ord.append(infos_fournisseurs[i][2][1])

fig, ax = plt.subplots()
ax.scatter(abs, ord)

for i, txt in enumerate(n):
    ax.annotate(txt, (abs[i], ord[i]))

plt.scatter(coord_depot[0], coord_depot[1], color='g') #dépôt en vert
plt.scatter(coord_usine[0], coord_usine[1], color='r') #usine en rouge
plt.show()

###
def plus_pres(i):
    list_dist = []
    for j in range(nb_fournisseurs):
        if (j!=i):
            list_dist.append(distance_heuristique(i, j))
    min = list_dist[0]
    ind = 0
    for k in range(len(list_dist)):
        if list_dist[k] < min and k!=i:
            min = list_dist[k]
            ind = k
    return(ind)

l_plus_proche = [plus_pres(i) for i in range(nb_fournisseurs)]

    
