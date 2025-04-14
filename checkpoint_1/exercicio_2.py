'''Questão 2 [1,5 pontos] Crie um programa em Python que solicite ao usuário três comprimentos de
lados de um triângulo. Em seguida, mostre qual é o tipo do triângulo de acordo com as seguintes
definições:
● Equilátero (todos os lados iguais)
● Isósceles (dois lados iguais)
● Escaleno (todos os lados diferentes)
'''

#ENTRADA
lado1 = float(input("DIGITE O PRIMEIRO LADO DO TRIÂNGULO: "))
lado2 = float(input("DIGITE O SEGUNDO LADO DO TRIÂNGULO: "))
lado3 = float(input("DIGITE O TERCEIRO LADO DO TRIÂNGULO: "))

#PROCESSAMENTO / SAÍDA
if (lado1 == lado2 and lado2 == lado3):
    print("O TRIÂNGULO É EQUILÁTERO.")
elif (lado1 != lado2 and lado2 != lado3 and lado1 != lado3):
    print("O TRIÂNGULO É ESCALENO.")
else:
    print("O TRIÂNGULO É ISÓSCELES.")