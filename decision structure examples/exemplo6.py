'''
Criar um menu de opções para realizar 3 operações:
1. Somar 2 números inteiros.
2. Subtrair 2 número inteiros.
3. Multiplicar 2 números inteiros.
'''

#Estrutura de decisão: Match...Case.

print ("^v^v^vMENU DE OPÇÕES^v^v^v")
print ("1. Somar os 2 números.")
print ("2.Subtrair os 2 números.")
print ("3. Multiplicar os 2 números.")

opcao = int(input("Digite a opção desejada (1 a 3): "))
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

match opcao:
    case 1 :
        soma = num1 + num2
        print (f"A soma dos números é: {soma}")
    case 2:
        sub = num1 - num2
        print (f"A subtração dos números é: {sub}")
    case 3:
        mult = num1 * num2
        print (f"A multiplicação dos números é: {mult}")
    case _:
        print (f"Opção Inválida")