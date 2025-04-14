'''Questão 4 [1,5 pontos] Escreva um programa que solicite ao usuário os dados de uma compra
(nome do produto, preço e quantidade), escreva o nome do produto comprado e o valor total a ser
pago naquele produto, considerando que são oferecidos descontos pelo número de unidades
compradas, segundo a tabela abaixo:
• Até 10 unidades: valor total
• de 11 a 20 unidades: 10% de desconto
• de 21 a 50 unidades: 20% de desconto
• acima de 50 unidades: 25% de desconto'''


#Entrada
nome_produto = input("DIGITE O NOME DO PRODUTO: ")
preco_produto = float(input("DIGITE O VALOR DO PRODUTO: R$ "))
quantidade_produto = int(input("DIGITE A QUANTIDADE DE PRODUTOS: "))

#Processamento

if (quantidade_produto <= 10):
    valor_total = preco_produto * quantidade_produto * 1 #valor total
elif (quantidade_produto <= 20):
    valor_total = preco_produto * quantidade_produto * 0.90 #10% desconto
elif (quantidade_produto <= 50):
    valor_total = preco_produto * quantidade_produto * 0.80 #20% desconto
elif quantidade_produto > 50:
    valor_total = preco_produto * quantidade_produto * 0.75 #25 desconto
else:
    print("QUANTIDADE INVÁLIDA")

#Saída
print(f"PRODUTO: {nome_produto} | QUANTIDADE: {quantidade_produto} | VALOR TOTAL: R$ {valor_total:.2f}")