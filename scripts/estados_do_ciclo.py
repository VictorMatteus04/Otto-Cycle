#Estado 1: Compressão
v_c = v_s / (taxa_compressao - 1) #Volume de folga no cilindro
v1 = v_c + v_s
t1 = 750 #Temperatura dentro do cillindro durante compressão(600K-800K)
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
t3 = 2300 # Temperatura durante explosão(2300K-2700K)
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