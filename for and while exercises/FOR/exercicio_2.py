'''2· Escreva um programa em Python que solicite 10 valores inteiros ao usuário e mostre quantos 
desses valores lidos são negativos. Para tal, utilize a estrutura de repetição “for”.'''

negativos = 0

for cont in range(10):
    num = int(input("DIGITE UM NÚMERO INTEIRO: ")) #ENTRADA
    if (num < 0): #PROCESSAMENTO
        negativos += negativos + 1

print(f"VOCÊ DIGITOU {negativos} VALORES NEGATIVOS.") #SAIDA