def job_shop_scheduling(jobs_data):
    # Todo: Inicialização da solução, dos contadores de maquinas e trabalhos e dos verificadores possiveis
    jobs_solution = []  # Solução
    id_in_solution = []  # Verificador (Se o id de um job já esta na solução)
    quant_maqui = len(jobs_data)  # Quantas maquinas exitem no array recebido
    quant_jobs = len(jobs_data[0])  # Quantos job's existem no array recebido
    for a in range(quant_maqui):  # Inicializa a Solução
        jobs_solution.append([])  # Coloca apenas as maquinas na solução
    for i in range(0, quant_jobs):  # Faz a contagem de avanço de tempo
        jobs_data[0][i][1] = 0  # Padroniza o inicio de um job na primeira maquina como 0
        for j in range(1, quant_maqui):
            jobs_data[j][i][1] = jobs_data[j - 1][i][1] + jobs_data[j - 1][i][
                2]  # Tempo de inicio do Trabalho do Job i na Maquina j é a soma do inicio e da duração  # do trabalho anterior no job i.
    # Todo: Parte gulosa da coisa. Ele vai percorrer todo o meu vetor de Jobs (Até o vetor estar 'vazio').
    # Todo: A cada iteração, ele vai pegar o job com menor tempo total de execução e adicionar na solução.
    # Todo: Após adicionar na solução, ele vai avançar o tempo do projeto baseado no job adicionado na solução.
    for j in range(0, quant_jobs):
        id_menor_tempo = 0  # Job com o menor id da rodada
        for i in range(0, quant_jobs):
            if i not in id_in_solution:  # Procura o proximo job que não está na solução
                id_menor_tempo = i  # Define o job inicial da rodada como ele e continua o for
                break
        # Todo: Procura o job com o menor tem de execução total
        for i in range(0, quant_jobs):
            if i not in id_in_solution:  # Verifica se ele já esta na solução
                if jobs_data[-1][i][1] + jobs_data[-1][i][2] <= jobs_data[-1][id_menor_tempo][1] + \
                        jobs_data[-1][id_menor_tempo][2]:
                    # Verifica se o tempo de execução do job i é menor ou igual que o tempo de execução do job id_menor_tempo
                    id_menor_tempo = i  # Se for, o novo job id_menor_tempo é o job i
        # Todo: Adiciana o Job encontrado na solução (isso garante que os jobs serão sequenciais)
        id_in_solution.append(id_menor_tempo)  # Adiciona o id do job que será adicionado na solução
        for l in range(0, quant_maqui):  # Adiciona o Job na solução
            jobs_solution[l].append(jobs_data[l][id_menor_tempo])
        # Todo: Avanço de tempo para manutenção do espaço-tempo (mexer com isso não é brincadeira)
        last_solution_job = []  # Ultimo Job colocado na solução
        for i in range(0, quant_maqui):
            last_solution_job.append(jobs_solution[i][-1])
        for i in range(0, quant_jobs):  # Avanço de tempo
            if i not in id_in_solution:  # Não avança quem já esta na solução
                jobs_data[0][i][1] = last_solution_job[0][1] + last_solution_job[0][2]
                # Avança o Trabalho do job i na maquina 0.
                for j in range(1, quant_maqui):  # Avança o Trabalho do job i nas outras maquinas
                    j1 = jobs_data[j - 1][i][1] + jobs_data[j - 1][i][2]
                    # j1 = Tempo de execução do Trabalho do job i na maquina anterior
                    j2 = last_solution_job[j][1] + last_solution_job[j][2]
                    # j2 = Tempo de execução do Trabalho do job anterior na mesma maquina
                    if j1 >= j2:  # Verifica se a maquina já esta livre
                        jobs_data[j][i][1] = j1  # Se esta livre, ocupa
                    else:
                        jobs_data[j][i][1] = j2  # Se não esta livre, espera desocupar
    return jobs_solution


# Todo: Todo job (Coluna) tem um trabalho (Elemento da Matriz) em uma maquina (Linha).
# Todo: Trabalho = [id_job, Tempo de inicio, Duração].
# Todo: O tempo de inicio é um valor inteiro positivo ou negativo (Valor padrão: 0).
# Todo: Para que um job seja reconhecido, é necessario, que quando não exista
# Todo: um trabalho em uma maquina, seja feito um trabalho fantasma no formato [id, 0, 0].
jd = [[[0, 0, 4], [1, 0, 8], [2, 0, 10], [3, 0, 10]],
      [[0, 0, 5], [1, 0, 4], [2, 0, 8], [3, 0, 10]],
      [[0, 0, 9], [1, 0, 0], [2, 0, 0], [3, 0, 10]]]
for ki in range(len(jd)):
    print(str(jd[ki]))
print("----------------------------")
maq = job_shop_scheduling(jd)
for ki in range(len(jd)):
    print(str(maq[ki]))
