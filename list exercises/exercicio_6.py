'''Escreva um programa em Python que crie uma lista de 10 funcionários, utilizando o conceito de dicionários, contendo os seguintes dados:

o Nome;

o Cargo;

o Salário.

Depois da lista criada, exiba todos os funcionários com seus dados um debaixo do outro.

OBS: o programa deverá solicitar que o usuário informe os dados para alimentar a lista de dicionário.'''

lista_funcionarios = []

for i in range (5):
    try:
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("O salário deve ser numérico")
    else:
        funcionario = {
        'Nome':nome,
        'Cargo':cargo,
        'Salário':salario
    }
        lista_funcionarios.append(funcionario)
    finally:
        print("Operação finalizada.")
#Saída
for funcionario in lista_funcionarios:
    for chave,valor in funcionario.items():
        print (f"{chave}: {valor}")
    print (f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")