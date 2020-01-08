from kmeans import corresp
from fct_cout import cout
from solution_triviale import sous_traites_bool
from parseur_kiro import infos_fournisseurs
from constitution_groupe import *


## groupes en faisant varier les clusterings
couts_solution = []
solutions=[]

for i in range(2, 100):
    x=[]
    corresp=[]
    for k in range(len(infos_fournisseurs)):
        if sous_traites_bool[k]==0:
            x.append([infos_fournisseurs[k][2][0],infos_fournisseurs[k][2][1]])
            corresp.append(k)
    
    x=np.array(x)
    kmeans = KMeans(i)
    kmeans.fit(x)
    clustos=kmeans.labels_
    
    GROUP = constit_groupe_simple(isolement(clustos, i))
    
    tournees=cree_tournees(GROUP)
    
    solution = [sous_traites_bool, tournees, GROUP]
    
    couts_solution.append(cout(solution))
    solutions.append(solution)

## donne les N meilleures solutions
indice_min = 0
N=5
N_meilleurs = []
couts_N_meilleurs = []
for j in range(N):
    cout_sol = 10000000000000
    for i in range(len(couts_solution)):
        if couts_solution[i] < cout_sol and (i not in N_meilleurs):
            cout_sol = couts_solution[i]
            indice_min = i
    N_meilleurs.append(indice_min)
    couts_N_meilleurs.append(cout_sol)

print(N_meilleurs)
print(couts_N_meilleurs)