'''
Escreva um programa que solicite três valores inteiros (representados pelas variáveis A, B e C), calcule e apresente como resultado final o valor da soma dos quadrados dos três valores lidos.
'''


#ENTRADA
valor_A = int(input("Digite o valor de (A): "))
valor_B = int(input("Digite o valor de (B): "))
valor_C = int(input("Digite o valor de (C): "))
quadrado_A = valor_A ** 2
quadrado_B = valor_B ** 2
quadrado_C = valor_C ** 2

#PROCESSAMENTO
soma_quadrado = (valor_A ** 2) + (valor_B ** 2) + (valor_C ** 2)

#SAÍDA
print(f" Aqui estão os resultados: {valor_A}² = {quadrado_A}. {valor_B}² = {quadrado_B}. {valor_C}² = {quadrado_C}. O resultado da soma dessas exponenciações é: {soma_quadrado}")