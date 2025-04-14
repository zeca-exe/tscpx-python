'''Questão 5 [1,5 pontos] Faça um programa que solicite um número inteiro e execute as operações
listadas a seguir de acordo com a escolha do usuário:
Escolha do usuário Operação
1 Par ou ímpar
2 Múltiplo ou não de 3
3 Positivo, negativo ou neutro
'''

#ENTRADA
num = int(input("POR FAVOR, DIGITE UM NÚMERO INTEIRO: "))
print("QUAL OPERAÇÃO VOCÊ DESEJA EXECUTAR?")
print("1 - DESCUBRIR SE O NÚMERO É PAR OU IMPAR")
print("2 - DESCOBRIR SE O NÚMERO É MULTIPLO OU NÃO DE 3")
print("3 - DESCOBRIR SE O NÚMERO É POSITIVO, NEGATIVO OU NEUTRO")
opcao = int(input("AGORA SELECIONE UMA OPÇÃO (1 - 3): "))

#PROCESS
match opcao:
    case 1:
        if (num % 2 == 0):
            print(f"O NÚMERO {num} É PAR!")
        else:
            print(f"O NÚMERO {num} É IMPAR!")
    case 2:
        if (num % 3 == 0):
            print(f"O NÚMERO {num} É MULTIPLO DE 3")
        else:
            print(f"O NÚMERO {num} NÃO É MULTIPLO DE 3")
    case 3:
        if (num > 0):
            print(f"O NÚMERO {num} É POSITIVO")
        elif (num < 0):
            print(f"O NÚMERO {num} É NEGATIVO")
        else:
            print(f"O NÚMERO {num} É NEUTRO")
    case _:
        print("OPÇÃO INVÁLIDA")
