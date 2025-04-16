'''Escreva um programa que solicite uma temperatura na escala Fahrenheit,
 faça a conversão e exiba a temperatura equivalente em Celsius. Celsius = 5/9 * (F - 32).'''

#ENTRADA

fahre = float(input("Digite a temperatura em Fahrenheit: "))

#PROCESSAMENTO
celsius = (5 / 9) * (fahre - 32)

#SAÍDA
print(f"A temperatura de {fahre:.2f}°F equivale a {celsius:.2f}°C.")