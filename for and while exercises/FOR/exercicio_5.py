'''5· Faça um programa em Python que mostre na tela os números divisíveis por 6 compreendidos entre 50 e 100. 
(Considere os números 50 e 100 e utilize estruturas de repetição).'''

print("NÚMEROS DIVISÍVEIS POR 6 ENTRE 50 E 100:")
for num in range(50, 101): 
    if num % 6 == 0:
        print(num)