'''1. Escreva um programa em Python para ler 10 valores e escrever
quantos desses valores lidos estão no intervalo [10,20]
(incluindo os valores 10 e 20 no intervalo)
e quantos deles estão fora deste intervalo.
Nesse caso, utilize a estrutura de repetição “for”.'''

dentro = 0
fora = 0

for cont in range(10):
    num = int(input("Digite um número inteiro: ")) #ENTRADA
    if (num >= 10 and num <=20):
        dentro += 1
    else:
        fora += 1

print(f"Você digitou {dentro} valores que estão entre 10 e 20 e {fora} valores estão fora.") #SAIDA