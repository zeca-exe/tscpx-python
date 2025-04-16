'''
Escreva um programa que solicite a base e a altura de um triângulo, calcule sua área por meio da fórmula: area = (base x altura)/2. Por fim, exiba a área do triângulo.
'''

#ENTRADA
base_triangulo = float(input("Digite a base do triângulo: "))
altura_triangulo = float(input("Digite a altura do triângulo: "))
#PROCESSAMENTO
area_triangulo = (base_triangulo * altura_triangulo) / 2
#SAÍDA
print (f"A área do seu triângulo é de: {area_triangulo:.2f} m²")