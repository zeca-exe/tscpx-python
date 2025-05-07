'''
1.Faça um programa que solicite ao usuário 15 números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
OBS: é obrigatório a utilização do “for”.
'''
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

for cont in range(15):
    num = int(input("Digite um número inteiro: "))
    if (num >= 0 and num <= 25):
        intervalo1+=1
    elif (num <= 50):
        intervalo2+=1
    elif (num <= 75):
        intervalo3+=1
    elif (num <= 100):
        intervalo4+=1

print(f"Você digitou {intervalo1} números dentro do intervalo [0-25]")
print(f"Você digitou {intervalo2} números dentro do intervalo [26-50]")
print(f"Você digitou {intervalo3} números dentro do intervalo [51-75]")
print(f"Você digitou {intervalo4} números dentro do intervalo [76-100]")