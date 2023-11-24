# Função para calcular o trabalho em um ciclo
def calcular_trabalho(pressures, volumes):
    work = 0
    work_stages = []

    for i in range(3):  # Percorrer os três estágios: compressão, combustão e expansão
        delta_v = volumes[i+1] - volumes[i]
        stage_work = pressures[i] * delta_v
        work += stage_work
        work_stages.append(stage_work)
    
    return work, work_stages

# Rotações por segundo
rpm = 3000
rps = rpm / 60  # Converter rotações por minuto para rotações por segundo

# Calcular o trabalho em um ciclo e a potência
trabalho_por_ciclo, trabalho_por_etapa = calcular_trabalho(pressoes, volumes)
potencia = trabalho_por_ciclo * rps

# Eficiência térmica
eficiencia = (1 - 1 / pow(taxa_compressao, gamma - 1)) * 100

