from kmeans import corresp
from fct_cout import cout
from solution_triviale import sous_traites_bool
from parseur_kiro import infos_fournisseurs
from constitution_groupe import *


## groupes en faisant varier les clusterings
def groupes_variation_clustering(nb_iterations, sous_traites):
    solutions=[]
    for i in range(2, nb_iterations+2):
        
        corresp, x = correspondance(sous_traites)
        
        kmeans = KMeans(i)
        kmeans.fit(x)
        clustos=kmeans.labels_
        
        groupe0 = constit_groupe_simple(isolement(clustos, i, corresp))
        
        tournees0=cree_tournees(groupe0)
        
        solution0 = [sous_traites, tournees0, groupe0]
        
        solutions.append(solution0)
    return(solutions)

## donne les N meilleures solutions
def n_meilleures_sol(solutions, N):
    couts_solution=[]
    for x in solutions:
        couts_solution.append(cout(x))
    
    indice_min = 0
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
    return(N_meilleurs)
    
##
sous_traites_bool = sous_traites_avec_seuil(1)
solutions = groupes_variation_clustering(20, sous_traites_bool)
meilleure_sol_originale = solutions[n_meilleures_sol(solutions, 1)[0]]