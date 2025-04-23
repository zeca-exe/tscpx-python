'''Desenvolva um programa que solicite ao usuário um valor inteiro e apresente a tabuada de multiplicação de 1 até 10 para esse número.

Exemplo:

Digite um número inteiro positivo: 5

5 x1 =5

5 x2=10

5 x3=15

…

5 x10=50

OBS: é obrigatório utilizar a estrutura de repetição “for”.'''

#ENTRADA
num = int(input("Digite um número inteiro: "))
#PROCESSAMENTO/
for cont in range(11):
    mult = (num * cont)
    #SAÍDA
    print(f"{num} x {cont} = {mult}")