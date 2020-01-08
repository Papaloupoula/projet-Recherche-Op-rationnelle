from typing import Tuple, TextIO

class Instance:
    def __init__(self, file: TextIO):
        lines = file.readlines()
        #lines = [line.decode().rstrip() for line in lines]

        # first line is meta data
        metadata0 = lines[0].split(' ')

        if len(metadata0) != 6:
            raise Exception(
                "[INSTANCE] Wrong meta data length in instance, must be 6.")

        self.Q = int(metadata0[1])
        self.F = int(metadata0[3])
        self.H = int(metadata0[5])

        # second line is depot
        metadata1 = lines[1].split(' ')
        self.d = int(metadata1[1])

        # third line is usine
        metadata2 = lines[2].split(' ')
        self.u = int(metadata2[1])

        # providers
        self.providers = []

        for line in lines[3:3+self.F]:
            data = line.split(' ')
            cdock_cost = int(data[3])

            quantity = list(map(lambda x: int(x), data[5:5+self.H]))
            self.providers.append([cdock_cost, quantity])

        # matrice de correpondances
        size = self.F+2
        self.correspondences = [[0] * size for _ in range(size)]

        for line in lines[3+self.F:]:
            data = line.split(' ')

            self.correspondences[int(data[1])][int(data[2])] = int(data[4])


class Solution:
    def __init__(self, solution: str):

        lines = solution.split('\n')
        split_lines = [line.split(' ') for line in lines if len(line) > 0]

        # nombre de fournisseurs utilisés et leur liste
        self.x = int(split_lines[0][1])
        self.providers_cd = [int(f) for f in split_lines[0][3:]]

        # nombre de tourneés
        self.y = int(split_lines[1][1])

        # nombre de groupes
        self.z = int(split_lines[2][1])

        # liste des fournissuers par groupe
        self.groups = []
        for line in split_lines[3:3+self.z]:
            n = int(line[3])
            self.groups.append([int(line[5+i]) for i in range(n)])

        # liste des tournées
        self.tourne = []
        for line in split_lines[3+self.z:]:
            g = int(line[3])
            s = int(line[5])
            n = int(line[7])
            f = [[int(line[9+i*3]), int(line[10+i*3])] for i in range(n)]
            self.tourne.append([g, s, n, f])


def prepare_eval_data(instance_file: TextIO, solution_str: str) -> Tuple[Instance, Solution]:
    return Instance(instance_file), Solution(solution_str)


def check_solution(instance: Instance, solution: Solution) -> bool:

    # data for check
    x = solution.x
    y = solution.y
    z = solution.z
    solprov_cd = solution.providers_cd
    solgroups = solution.groups
    soltour = solution.tourne

    Q = instance.Q
    F = instance.F
    H = instance.H
    prov = instance.providers

    if x > F:
        raise Exception("Too much providers outsourced !")

    if z > len(prov)-x:
        raise Exception("Too much groups !")

    if len(soltour) != y:
        raise Exception("You don't have declared the right amount of tours !")

    if len(solgroups) != z:
        raise Exception("You don't have declared the right amount of groups !")

    for g in solgroups:
        if any(map(lambda x: x in solprov_cd, g)):
            print(g)
            raise Exception(
                "At least one group contains a provider already outsourced !")
        if any(map(lambda x: x > (F-1), g)):
            raise Exception(
                "At least one group contains a provider with an indice out of bounds !")

    for t in soltour:
        if t[0] >= z:
            raise Exception("At list one tour contains a group out of bounds")
        if t[1] >= H:
            raise Exception("There are only "+str(H)+" weeks")
        if t[2] != len(t[3]):
            raise Exception(
                "At list one tour has different amount of providers than the number declared")
        if any(map(lambda x: x not in solgroups[t[0]], [t[3][i][0] for i in range(len(t[3]))])):
            raise Exception(
                "At least one provider declared in a tour is not in the corresponding group !")
        if len([t[3][i][0] for i in range(len(t[3]))]) != len(set([t[3][i][0] for i in range(len(t[3]))])):
            raise Exception("One tour can pass only one time at a provider")
        if sum([t[3][i][1] for i in range(len(t[3]))]) > Q:
            raise Exception("At least one truck is overloaded !")

    quant = [[0]*len(prov) for _ in range(H)]
    for s in range(H):
        for t in soltour:
            if t[1] == s:
                for i in range(len(t[3])):
                    quant[s][t[3][i][0]] += t[3][i][1]

    for s in range(H):
        for j in range(len(prov)):
            if j not in solprov_cd:
                if quant[s][j] != prov[j][1][s]:
                    print('Fournisseur : ', j)
                    print('Semaine : ', s)
                    print(quant[s][j])
                    raise Exception("Total quantities are not respected !")

    return True


def evaluate_solution(instance: Instance, solution: Solution) -> int:

    # Q = instance.Q
    # F = instance.F
    # H = instance.H

    u = instance.u
    d = instance.d

    prov = instance.providers
    corr = instance.correspondences

    # cross docks costs
    solprov_cd = solution.providers_cd
    cd_cost = sum([prov[f][0] for f in solprov_cd])

    # tour costs
    soltour = solution.tourne
    t_cost = 0
    for t in soltour:
        t_cost += corr[d][t[3][0][0]]
        for i in range(len(t[3])-1):
            t_cost += corr[t[3][i][0]][t[3][i+1][0]]
        t_cost += corr[t[3][-1][0]][u]

    cost = cd_cost+t_cost
    return cost

fichiertxt = open('solution.csv', 'r')
filetxt = ''
for s in fichiertxt:
    filetxt += s
S = Solution(filetxt)


instance000 = open('usine.csv', 'r')

I = Instance(instance000)

check_solution(I,S)