'''7· Escreva um algoritmo que solicite dois números
e devolva quantos pares e ímpares há entre esses
dois números. Exemplo: entre 7 e 10 há 2 números pares e 2 números ímpares'''


#ENTRADA
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

par = 0
impar = 0



#PROCESSAMENTO
if (inicio < fim):
    for num in range(inicio, fim + 1):
        if num % 2 == 0:  #PAR
            par += 1
        else:  #IMPAR
            impar += 1
#SAÍDA
    print(f"Entre {inicio} e {fim} existem {par} números pares e {impar} números ímpares!")
else:
    print("O ínicio deve ser menor que o fim!")