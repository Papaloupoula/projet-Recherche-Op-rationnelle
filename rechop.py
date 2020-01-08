
from tournees import *
from sklearn.cluster import KMeans

solution=solution_triviale
cout=cout(solution_triviale)

for k in range(2,50):
    kmeans=KMeans(k)
    c=np.array(y)
    kmeans.fit(c)
    clust=kmeans.labels_
    a=isolement(clust,k)
    GROUP = constit_groupe_simple(a)
    tournees=[]
    for i in range(len(GROUP)):
        tournee(i,GROUP[i])
    candidat=[sous_traites_bool,tournees,GROUP]
    if cout(candidat)<cout:
        solution=candidat
        cout=cout(solution)

print(cout)

