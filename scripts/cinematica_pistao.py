def cinematica_pistao(diametro, curso, biela, taxa_compressao, angulo_inicial, angulo_final):
    # Parâmetros geométricos
    a = curso / 2  # Semi-curso do pistão
    R = biela / a  # Razão entre a biela e o semi-curso do pistão

    # Parâmetros de volume
    V_s = (math.pi) * (1/4) * pow(diametro, 2) * curso  # Volume de deslocamento
    V_c = V_s / (taxa_compressao - 1)  # Volume de folga

    angulo_inicial_rad = math.radians(angulo_inicial)  # Converter o ângulo inicial para radianos
    angulo_final_rad = math.radians(angulo_final)  # Converter o ângulo final para radianos

    num_valores = 50  # Número de pontos para discretizar o ciclo

    delta_theta = (angulo_final_rad - angulo_inicial_rad) / (num_valores - 1)  # Incremento angular
    V = []  # Lista para armazenar os volumes

    # Loop para calcular os volumes ao longo do ciclo
    for i in range(0, num_valores):
        theta = angulo_inicial_rad + i * delta_theta  # Ângulo atual
        termo1 = 0.5 * (taxa_compressao - 1)  # Primeiro termo comum nos cálculos
        termo2 = R + 1 - math.cos(theta)  # Segundo termo dependente do ângulo
        termo3 = pow(R, 2) - pow(math.sin(theta), 2)  # Terceiro termo dependente do ângulo
        termo3 = pow(termo3, 0.5)  # Raiz quadrada do terceiro termo
        # Cálculo do volume no ângulo atual e adição à lista
        V.append((1 + termo1 * (termo2 - termo3)) * V_c)

    return V  # Retorna a lista de volumes ao longo do ciclo
