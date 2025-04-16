'''
Escreva um programa que solicite o peso e a altura de uma pessoa, calcule o IMC (índice de massa corpórea) por meio da fórmula: IMC = peso/altura*altura. Por fim, exiba o valor do IMC.
'''

#ENTRADA
altura = float (input("Insira sua altura em metros: "))
peso = float (input("Insira seu peso em quilos: "))

#PROCESSAMENTO
imc = peso / altura ** 2

#SAÍDA
print(f"O seu Índice de Massa Corpórea é de: {imc:.2f}")

