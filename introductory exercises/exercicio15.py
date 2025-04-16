'''Escreva um programa que solicite 3 lados de um triângulo, calcule e mostre seu perímetro (soma dos lados).'''


#ENTRADA
ladoA = float(input("Digite o primeiro lado do triângulo: "))
ladoB = float(input("Digite o segundo lado do triângulo: "))
ladoC = float(input("Digite o terceiro lado do triângulo: "))

#PROCESSAMENTO
perimetro = ladoA + ladoB + ladoC

#SAÍDA
print(f"O perímetro do triângulo é: {perimetro:.2f}")