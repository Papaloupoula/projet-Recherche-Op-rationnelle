## Antiparseur

import csv as csv
def antiparseur(solution):
    liste_sous_trait = solution[0]
    id_sous_trait = []
    for i in range(len(liste_sous_trait)):
        if liste_sous_trait[i] == 1:
            id_sous_trait.append(i)
    nb_sous_trait = 0
    for el in liste_sous_trait:
        nb_sous_trait += el
    
    tournees = solution[1]
    nb_tournees = len(tournees)
    
    groupes = solution[2]
    nb_groupes = len(groupes)
    
    
    with open('solution.csv', 'w', newline='') as csvfile:
        solwriter = csv.writer(csvfile, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        solwriter.writerow(['x'] + [nb_sous_trait] + ['f'] + [id_sous_trait[i] for i in range(len(id_sous_trait))])
        solwriter.writerow(['y'] + [nb_tournees])
        solwriter.writerow(['z'] + [nb_groupes])
        for i in range(nb_groupes):
            groupe = groupes[i]
            row = ['c'] + [i] + ['n'] + [len(groupe)] + ['f']
            for f in range(len(groupe)):
                row = row + [groupe[f]]
            solwriter.writerow(row)
        for j in range(nb_tournees):
            tournee = tournees[j]
            row = ['p'] + [j] + ['g'] + [tournee[0]] + ['s'] + [tournee[1]] + ['n'] + [len(tournee[2])]
            for f in range(len(tournee[2])):
                row = row + ['f'] + [tournee[2][f]] + [tournee[3][f]]
            solwriter.writerow(row)


### Format des données
""""
solution = [sous_traitance, tournees, groupes]


1. sous_traitance
sous_traitance[i] = 0 si i n'est pas sous_traité
sous_traitance[i] = 1 s'il l'est


2. tournees
i_ème tournee = tournees[i]
alors :
tournee[0] = groupe de la tournée
tournee[1] = semaine de la tournée
tournee[2] = [fournisseurs visités, dans l'ordre]
tournee[3] = [qtés récupérées chez chaque fournisseur, dans l'ordre]

3. groupes
i_ème groupe = groupes[i]
groupe = [fournisseurs dans le groupes, 4 maximum]
""""