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
