'''
Escreva um programa que solicite o salário de um funcionário, faça o acréscimo de 20% sobre seu valor e exiba-o. DICA: para fazer o acréscimo, multiplique o valor do salário por 1,20.
'''

#ENTRADA
salario_bruto = float(input("Digite o salário do colaborador: "))
#PROCESSAMENTO
aumento = salario_bruto * 1.20
#SAÍDA
print(f"O salário final com o aumento de 20% é: R${aumento:.2f}")