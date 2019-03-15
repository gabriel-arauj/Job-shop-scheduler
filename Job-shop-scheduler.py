import collections
import itertools
# Abaixo, temos o modelo da matriz que deve ser inserida para o codigo trabalhar. Cada columm de listas representa um
# Job. Cada linha uma maquina. Cada tupla representa uma operação, contendo o id do Job, o tem tempo inicial (dese ser setado 0 no inicio),
# e o tempo de processamento.
# Em Jobs que não são operados por algumas das maquinas, complemente o local com um Job Fantasma: [Job_Id, 0, 0]
jobs_data2 = [                                       #Operação = (Job_id, initial_time, processing_Time)
    [[0, 0, 4], [1, 0, 8], [2, 0, 10], [3, 0, 20]],  #Maquina1
    [[0, 0, 5], [1, 0, 4], [2, 0, 8], [3, 0, 10]],   #Maquina2
    [[0, 0, 9], [1, 0, 0], [2, 0, 0], [3, 0, 5]],    #Maquina3
    [[0, 0, 3], [1, 0, 0], [2, 0, 11], [3, 0, 17]],  #Maquina4
    [[0, 0, 2], [1, 0, 9], [2, 0, 2], [3, 0, 15]]
]
# É contado a quantidade de maquinas do conjunto
quant_maquinas = len(jobs_data2)
# Cria-se uma lista para guardar todas as permutações de operações das maquinas.
all_permutations_maq = []
for i in range(0, quant_maquinas):
    all_permutations_maq.append([])

# nesse trecho é feito a permutação das operações. Após realizada, é atualizado o valor dos
# tempos inicias da primeira maquina, de tal forma que as operações são executadas sucessivamente, já que não tem precedencia.
# Após, as permutações são armazenadas na variavel criada previamente (all_permutations_maq)
for jobs_maq1 in list(itertools.permutations(jobs_data2[0])):
    maq = [[]]
    for j1 in jobs_maq1:
        a = []
        for j2 in range(0, len(j1)):
            a.insert(j2, j1[j2])
        maq[0].append(a)
    for i in range(1, len(jobs_maq1)):
        maq[0][i][1] = maq[0][i-1][1] + maq[0][i-1][2]
    all_permutations_maq[0].append(maq[0])


# Abaixo, é realizado a permutação das operações para as outras maquinas. Da mesma forma anterior, é realizado o calculo
# dos valores de inicio de cada atividade, de tal forma que é verificado se a operação seguinte é realizada acompanhando
# a operação anterior na mesma maquina, ou acompanhando a operação anterior do mesmo Job.
for i in range(1, len(all_permutations_maq)):
    for jobs_maq in list(itertools.permutations(jobs_data2[i])):
        maq25 = []
        for ai in jobs_maq:
            a = []
            for aj in range(0, len(ai)):
                a.insert(aj, ai[aj])
            maq25.append(a)
        all_permutations_maq[i].append(maq25)
    for linha in range(0, len(all_permutations_maq[i])):
        all_permutations_maq[i][linha][0][1] = all_permutations_maq[i-1][linha][0][2] + all_permutations_maq[i-1][linha][0][1]
        for columm in range(1, len(all_permutations_maq[i][linha])):
            atual = all_permutations_maq[i][linha][columm - 1][1] + all_permutations_maq[i][linha][columm - 1][2]
            anterior = all_permutations_maq[i-1][linha][columm][1] + all_permutations_maq[i - 1][linha][columm][2]
            if anterior < atual:
                all_permutations_maq[i][linha][columm][1] = atual
            else:
                all_permutations_maq[i][linha][columm][1] = anterior

# Aqui é procurado qual a sequencia de operações que tem o menor tempo de execução. Como a ultima operação da ultima
# maquina é a que indicará qual a menor sequencia, podemos diminuir a pesquisa para apenas esses valores.
min = all_permutations_maq[-1][0][-1][1] + all_permutations_maq[-1][0][-1][2]
ind_min = 0
for permution_last_maq in all_permutations_maq[-1]:
    if min > permution_last_maq[-1][1] + permution_last_maq[-1][2]:
        min = permution_last_maq[-1][1] + permution_last_maq[-1][2]
        ind_min = all_permutations_maq[-1].index(permution_last_maq)

# Exibição da sequencia de serviço que demora menos.
for result in all_permutations_maq:
    print(f"Maquina {all_permutations_maq.index(result)}: {result[ind_min]}")
