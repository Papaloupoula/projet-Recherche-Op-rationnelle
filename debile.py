# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:37:25 2019

@author: Charles
"""

#traitement débile

Q=13
a=0

x=[]
y=[]
z=[]

nbr_min_passages_camions=[]

for i in range(nb_fournisseurs):
    n=0
    for j in range(8):
        s=infos_fournisseurs[i][1][j]
        if (isinstance(s/Q, int)):
            a=s/Q
        else:
            a=int(s/Q) + 1
        n+=s
    nbr_min_passages_camions.append(n)

def cout_aller_retour(i):
    #cout pour faire depot -> fournisseur i -> usine
    return matrice_couts[nb_fournisseurs][i]+matrice_couts[i][nb_fournisseurs+1]

def cout_min_quand_on_soustraite_pas(i):
    return cout_aller_retour(i)*nbr_min_passages_camions[i]


sous_traitants=[]

for i in range (nb_fournisseurs):
    if (cout_min_quand_on_soustraite_pas(i)<infos_fournisseurs[i][0]):
        z.append([i])
        x.append(0)
    else:
        x.append(1)
        sous_traitants.append(i)

for i in range(len(z)):
    fournisseur=z[i][0]
    for s in range(horizon):
        quantite=infos_fournisseurs[fournisseur][1][s]
        nbrtournee=quantite
        if (nbrtournee%Q > 0):
            nbrtournee = int(nbrtournee/Q)+1
        else:
            nbrtournee = int(nbrtournee/Q)
        for j in range(nbrtournee):
            y.append([i,s,[fournisseur],[min(Q,quantite)]])
            quantite = quantite - min(Q,quantite)





### Cout
def coutance(solution):
    xsol=solution[0]
    ysol=solution[1]
    cout=0
    for i in xsol:
        cout+= i*infos_fournisseurs[i][0]
    for tournee in ysol:
        cout_tournee=matrice_couts[-2][tournee[2][0]]
        for i in range(len(tournee[2])-1):
            cout_tournee+=matrice_couts[tournee[2][i]][tournee[2][i+1]]
        cout_tournee+=matrice_couts[tournee[2][-1]][-1]
        cout+=cout_tournee
    return cout
 
### Solution débile
debile=[x,y,z]


### Amélioration de solution
def amelioration_solution(solution,cout_solution,amelioration):
    upgrade=solution
    candidat=amelioration(solution)
    if cout_solution>cout(candidat):
        upgrade=candidat
    return upgrade

### Fusion tournée
def fusion_possible(solution,i,j):
    ysol=solution[1]
    zsol=solution[2]
    if j>len(ysol)-1:
        return False
    if i>len(ysol)-1:
        return False
    tournee1=ysol[i]
    tournee2=ysol[j]
    for f1 in tournee1[2]:
        for f2 in tournee2[2]:
            if f1==f2:
                return False 
    if tournee1[1]==tournee2[1]:
        q1=sum(tournee1[3])
        q2=sum(tournee2[3])
        if (q1+q2)<=Q:
            g1=tournee1[0]
            g2=tournee2[0]
            if g1==g2:
                return True
            if len(zsol[g1])+len(zsol[g2])<5:
                return True
    return False

    
def fusion(base,i,j):
    solution=base
    ysol=solution[1]
    zsol=solution[2]
    tournee1=ysol[i]
    tournee2=ysol[j]
    g1=tournee1[0]
    g2=tournee2[0]
    if g1!=g2:
        for fournisseur in zsol[g2]:
            zsol[g1].append(fournisseur)
        for k in range(len(ysol)):
            if ysol[k][0]>g2:
                ysol[k][0]-=1
            if ysol[k][0]==g2:
                if g1>g2:
                    g1-=1
                ysol[k][0]=g1
        del zsol[g2]
    for baflonj in range(len(tournee2[2])):
        ysol[i][2].append(tournee2[2][baflonj])
        ysol[i][3].append(tournee2[3][baflonj])
    del ysol[j]
    return [solution[0],ysol,zsol]    

solution_boss=debile
cout=coutance(solution_boss)
print(cout)

for i in range(len(debile[1])):
    for j in range(len(debile[1])):
        if fusion_possible(solution_boss,i,j):
            upgrade=fusion(solution_boss,i,j)
            cout_candidat=coutance(upgrade)
            if cout>cout_candidat:
                print("changement")
                solution_boss=upgrade
                cout=cout_candidat

print(cout)
    