from math import *
### Calcul des coûts si on ne sous-traite pas

# on commence par calculer le nombre minimal de passages de camions devant être faits pour chaque fournisseur

nbr_min_passages_camions=[]

for i in range(nb_fournisseurs):
    n=0
    qtes_fournies = infos_fournisseurs[i][1]
    for j in range(horizon):
        bibi_semaine = qtes_fournies[j]
        nb_passages_semaine = ceil(bibi_semaine/Q) # arrondi à l'entier supérieur (module math)
        n+=nb_passages_semaine
    nbr_min_passages_camions.append(n)
    del n
    del nb_passages_semaine
    del bibi_semaine
    del qtes_fournies

def cout_aller_retour(i):
    #cout pour faire depot -> fournisseur i -> usine
    return matrice_couts[nb_fournisseurs][i]+matrice_couts[i][nb_fournisseurs+1]

def cout_min_quand_on_soustraite_pas(i):
    return cout_aller_retour(i)*nbr_min_passages_camions[i]

###
sous_traites_bool = []
for i in range(nb_fournisseurs):
    if (cout_min_quand_on_soustraite_pas(i)<infos_fournisseurs[i][0]):
        sous_traites_bool.append(0)
    else:
        sous_traites_bool.append(1)
# sous_traites_bool[i] = 1 : on sous-traite i, 0 sinon

groupes = []
for i in range(nb_fournisseurs):
    if sous_traites_bool[i]==0:
        groupes.append([i]) #i forme un groupe d'1 élément

tournees = []
for i in range(len(groupes)):
    fournisseur = groupes[i][0]
    for sem in range(horizon):
        qte_a_recup = infos_fournisseurs[fournisseur][1][sem]
        nb_camions = ceil(qte_a_recup/Q)
        for j in range(nb_camions):
            qte_ds_camion = min(qte_a_recup, Q)
            tournee = [i, sem, [fournisseur], [qte_ds_camion]]
            qte_a_recup -= qte_ds_camion
            tournees.append(tournee)
            del qte_ds_camion
            del tournee
        del nb_camions
        del qte_a_recup
    del fournisseur


solution_triviale = [sous_traites_bool, tournees, groupes]