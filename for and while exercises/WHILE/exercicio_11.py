'''11 · Desenvolva um programa que solicite números inteiros ao usuário e calcule
a soma deles até que o 0 seja digitado.
'''
#ENTRADA
soma = 0
num = int(input("DIGITE UM NÚMERO PARA SOMAR e 0 PARA MOSTRAR O RESULTADO DA SOMA: "))
#PROCESSAMENTO
while (num !=0): #ENQUANTO O num FOR DIFERENTE DE 0
    soma+=num
    num = int(input("DIGITE UM NÚMERO PARA SOMAR e 0 PARA MOSTRAR O RESULTADO DA SOMA: "))
#SAÍDA
print(f"O RESULTADO DA SOMA DOS NÚMEROS DIGITADO É {soma}")