import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

# Entrada de dados
gamma = 1.4 #calor específico do ar 

# Propriedades geométricas do motor
print('\n')
print(80*'=')
diametro = float(input('Insira a medida do diâmetro (m): '))
curso = float(input('Insira o curso do motor (m): '))
biela = float(input('Insira a medida da biela (m): '))
taxa_compressao = float(input('Insira a taxa de compressão: '))
print(80*'=')
print('\n')

# Cálculo de volume de deslocamento do pistão(cilindrada)
v_s = (math.pi/4) * pow(diametro, 2) * curso  #Volume de deslocamento do pistão(cilindrada)

#Estado 1: Compressão
v_c = v_s / (taxa_compressao - 1) #Volume de folga no cilindro
v1 = v_c + v_s
t1 = 2300 #Temperatura dentro do cillindro durante compressão(2300K-2500K)
p1 = 101000 #Pressão durante a compressão (Pa)

#Estado 2:Adição de Calor
v2 = v_c
p2 = p1 * pow(v1, gamma) / pow(v2, gamma)
rhs = p1 * v1 / t1
t2 = p2 * v2 / rhs
V_compressao = cinematica_pistao(diametro, curso, biela, taxa_compressao, 180, 0)
constante = p1 * pow(v1, gamma)
P_compressao = []

for v in V_compressao:
    P_compressao.append(constante / pow(v, gamma))

#Estado 3 - Expansão/Combustão
t3 = 2500 # Temperatura durante explosão(2300K-2700K)
v3 = v2
rhs = p2 * v2 / t2
p3 = rhs * t3 / v3
V_expansao = cinematica_pistao(diametro, curso, biela, taxa_compressao, 0, 180)
constante = p3 * pow(v3, gamma)
P_expansao = []

for v in V_expansao:
    P_expansao.append(constante / pow(v, gamma))
    
#Estado 4 - Rejeição de Calor
v4 = v1
p4 = p3 * pow(v3, gamma) / pow(v4, gamma)
t4 = p4 * v4 / rhs

#Salva valores em listas
pressoes = [p1, p2, p3, p4]
temperaturas = [t1, t2, t3, t4]
volumes = [v1, v2, v3, v4]

# Rotações por segundo
rpm = 3000
rps = rpm / 60  # Converter rotações por minuto para rotações por segundo

# Calcular o trabalho em um ciclo e a potência
trabalho_por_ciclo, trabalho_por_etapa = calcular_trabalho(pressoes, volumes)
potencia = trabalho_por_ciclo * rps

# Eficiência térmica
eficiencia = (1 - 1 / pow(taxa_compressao, gamma - 1)) * 100


# Criar um DataFrame do Pandas
data = {
    'Temperatura (K)': temperaturas,
    'Pressão (Pa)': pressoes,
    'Volume (m^3)': volumes,
}

df = pd.DataFrame(data,index = [1, 2, 3, 4])

# Imprimir o DataFrame
print('\n')
print(80*'=')
print(df)
print(80*'=')

print('\n')

# Imprime informações de Energia do Ciclo
print(80*'=')
print('Trabalho durante a Expansão: {:.2f}(J)'.format(trabalho_por_etapa[2]))
print('Trabalho durante a Compressão: {:.2f}(J)'.format(trabalho_por_etapa[0]))
print('Trabalho Total por Ciclo: {:.2f}(J)'.format(trabalho_por_ciclo))
print('A potência fornecida pelo cilindro a {} rpm é igual a {:.2f}W'.format(rpm,potencia))
print('A Eficiência do Ciclo para uma Taxa de Compressão(Cr = {:.2f}) é de {:.2f} %.'.format(taxa_compressao, eficiencia))
print(80*'=')
print('\n')

#Plotando Ciclo Otto
plt.plot([v2, v3], [p2, p3])  # Adição de calor a pressão constante
plt.plot(V_compressao, P_compressao)  # Compressão
plt.plot(V_expansao, P_expansao)  # Expansão
plt.plot([v1, v4], [p1, p4])  # Rejeição de calor a pressão constante
plt.plot(v1, p1, 'o')  # Ponto inicial
plt.plot(v2, p2, 'o')  # Segundo ponto
plt.plot(v3, p3, 'o')  # Terceiro ponto
plt.plot(v4, p4, 'o')  # Quarto ponto
plt.title('Ciclo Otto para Taxa de Compressão(Cr) = {:.2f}'.format(taxa_compressao))
plt.xlabel('Volume em {}'.format(r'$m^3$'))
if taxa_compressao >= 5:
    plt.ylabel('Pressão em MPa') 
else:
    plt.ylabel('Pressão em Pa')
plt.legend(('Adição de Calor', 'Expansão', 'Compressão', 'Rejeição de Calor'))
plt.grid(True)
plt.tight_layout()
plt.show()

#Fim do programa
print('O programa foi executado com sucesso')