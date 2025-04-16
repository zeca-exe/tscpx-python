'''
Escreva um programa que solicite 2 números inteiros,
faça a soma, subtração e multiplicação. Por fim, mostre
os resultados.
'''

#ENTRADA
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite um segundo número inteiro: "))

#PROCESSAMENTO
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

#SAÍDA
print(f"O resultado da soma é:{soma}")
print(f"O resultado da subtração: {subtracao}")
print(f"O resultado da multiplicação: {multiplicacao}")