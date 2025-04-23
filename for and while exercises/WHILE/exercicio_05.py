'''Desenvolva um programa que solicite números inteiros ao usuário até que o 0 seja digitado. Em seguida, apresente o total de elementos ímpares digitados e o percentual do valor total de números ímpares em relação à quantidade total de números. OBS: é obrigatório utilizar a estrutura de repetição “while”.'''

total_num = 0
impares = 0

while True:
    num = int(input("Digite um número inteiro:"))
    if (num == 0):
        break
    if (num > 0):
        total_num+=1
        if (num % 2 != 0):
            impares+=1

    else:
        print ("O número deve ser positivo!")

print (f"Foram digitados {impares} números impares.")
percen_impares = (impares / total_num) * 100

print (f"Percentual de números impares é de {percen_impares:.2f}% números impares.")
