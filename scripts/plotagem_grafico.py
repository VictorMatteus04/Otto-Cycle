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
