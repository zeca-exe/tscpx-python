'''
2. Uma academia deseja fazer um censo entre seus clientes para descobrir o
mais alto e o mais baixo. Para isto, escreva um programa que solicite ao usuário o nome e a altura
de cada cliente. O final da digitação de dados deve acontecer quando o usuário digitar 0 (zero) na
altura. Após a digitação dos dados, o programa deverá exibir:
a) o nome e altura do cliente mais alto;
b) o nome e altura do cliente mais baixo;
OBS: é obrigatório a utilização do “while”. NÃO é permitido o uso de listas ou qualquer outro tipo
de armazenamento de dados.
'''

altura = float(input("Insira a altura do cliente [0 PARA SAIR]: "))
mais_alto = altura
mais_baixo = altura
nome_mais_alto = ""
nome_mais_baixo = ""

while (altura != 0):
    if (altura > 0):
        nome = input("Digite o nome do cliente: ")
        # Descobrir a maior altura
        if (altura > mais_alto):
            mais_alto = altura
            nome_mais_alto = nome
        if (altura < mais_baixo):
            mais_baixo = altura
            nome_mais_baixo = nome
    else:
        print("[ERRO] A altura deve ser um número positivo [ERRO]")

    altura = float(input("Insira a altura do cliente [0 PARA SAIR]: "))


print(f"CLIENTE MAIS ALTO: {nome_mais_alto} | {mais_alto} metros.")
print(f"CLIENTE MAIS BAIXO: {nome_mais_baixo} | {mais_baixo} metros.")
