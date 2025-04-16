'''10 · Escreva um programa que calcule o somatório de
todos os números pares em um intervalo definido pelo usuário.
Ex: para inicio = 2 e fim = 10 o somatório é 2+4+6+8+10. OBS: utilize o “for”.'''

#ENTRADA
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
#PROCESSAMENTO
soma = 0

if (inicio < fim ):
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            soma += num
    print(f"A soma dos números pares entre {inicio} e {fim} é: {soma}")#SAÍDA
else:
    print(f"[ERRO] INICÍO DEVE SER SEMPRE MENOR DO QUE O FIM! [ERRO]")

