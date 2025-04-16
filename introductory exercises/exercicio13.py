'''
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para solicitar ao usuário o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.
'''
#ENTRADA
cdf = float(input("Digite o custo de fábricação do automóvel: "))#cdf=custo de fabricação
distribuidor = 0.28
impostos = 0.45


#PROCESSAMENTO
valor = cdf + (cdf * distribuidor) + (cdf * impostos)

#SAÍDA
print(f"O custo final do automóvel para um consumidor é de: R$ {valor:.2f} reais")
