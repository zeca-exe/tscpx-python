'''8· Desenvolva um programa para calcular a média salarial dos funcionários da empresa XXX, 
para isso seu programa deverá solicitar o nome e salário dos 5 funcionários que trabalham nessa empresa. 
Ao final seu programa deverá calcular a média dos salários e exibir na tela as seguintes informações: 
(use 2 casas decimais na exibição dos números)
    o A média salarial dos funcionários da empresa XXX é _______

    o O nome e o salário do funcionário que recebe o menor salário

    o O nome e o salário do funcionário que recebe o maior salário
'''
# ENTRADA
nome_empresa = input("DÍGITE O NOME DA EMPRESA:")
soma_salario = 0

# PROCESSAMENTO
for cont in range(5): #CONT VARIADO DE 0 A 4 (5 vezes)
    funcionario = input(f"Insira o nome do {cont + 1}º colaborador:")
    salario = float(input(f"Insira o salário do {cont + 1}º colaborador:"))
    soma_salario +=salario
    if (cont==0): # PRIMEIRA VEZ [PRIMEIRO SALARIO DIGITADO]
        maior_salario = salario
        menor_salario = salario
        nome_maior = funcionario
        nome_menor = funcionario
    else: #CONT FOR MAIOR QUE 0
        #ENCONTRAR O MAIOR SALARIO
        if (salario > maior_salario):
            maior_salario = salario
            nome_maior = funcionario
        if (salario < menor_salario):
            menor_salario = salario
            nome_menor = funcionario


media_salario = soma_salario / 5
# SAÍDA
print(f"A média salarial dos colaboradores da empresa {nome_empresa} é R$ {media_salario:.2f}")

print(f"{nome_menor} tem o menor de salário (R$ {menor_salario:.2f})")
print(f"{nome_maior} tem o menor de salário (R$ {maior_salario:.2f})")

