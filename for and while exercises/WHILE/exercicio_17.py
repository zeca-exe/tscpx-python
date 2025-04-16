'''17 · Escreva um programa que contenha o seguinte menu:

Opção 1: Verificar e exibir se um número x é ou não divisível por 6;

Opção 2: Calcular o fatorial do número x;

Opção 3: Exibir todos os inteiros de 1 até um número x.

O programa deverá solicitar ao usuário a leitura de um número x e a opção desejada até que o usuário digite “N” para
 encerrar o programa. OBS: o programa deverá solicitar o número e a opção enquanto do usuário escolha “S”.'''


resp = "s"

while (resp == "s"):

    print ("===SELECIONE UMA DAS OPÇÕES===")
    print("1 - VERIFICAR E EXIBIR SE UM NÚMERO X É OU NÃO DIVISÍVEL POR 6.")
    print("2 - CALCULAR O FATORIAL DO NÚMERO X.")
    print("3 - EXIBIR TODOS OS NÚMEROS INTEIROS DE 1 ATÉ UM NÚMERO X.")
    opcao = int (input("DIGITE A OPÇÃO DESEJADA: "))


    if (opcao >= 1 and opcao <=3):
        x = int(input("DIGITE UM NÚMERO: "))
        match opcao:
            case 1:
                if (x % 6 == 0):
                    print(f"O NÚMERO {x} É DIVISÍVEL POR 6")
                else:
                    print(f"O NÚMERO {x} NÃO É DIVISÍVEL POR 6")
            case 2:
                fat = 1
                for cont in range (1, x+1):
                    fat*=cont
                print (f"O FATORIAL DE {x} É {fat}")
            case 3:
                if (x > 0):
                    for cont in range (1,x+1):
                        print (cont)
                else:
                    print("O NÚMERO DEVE SER MAIOR QUE ZERO!")
    else:
        print("OPÇÃO INVÁLIDA!")
    resp = input("DESEJA CONTINUAR? [S]SIM / [N] NÃO:" )
