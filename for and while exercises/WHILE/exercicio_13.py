'''13 · Mostrar todos os inteiros entre dois números
digitados pelo usuário.
Exemplo: usuário digita os números 8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.'''


inicio = int(input("DIGITE O INÍCIO DO INTERVALO: "))
fim = int(input("DIGITE O FIM DO INTERVALO: "))


if (inicio < fim):
    cont = inicio + 1


    while (cont < fim):
        print(cont)
        cont+=1
else:
    print ("[ERRO] O INICÍO DEVE SER SEMPRE MENOR QUE O FIM [ERRO]")

