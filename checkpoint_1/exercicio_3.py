'''Questão 3 [2,0 pontos] As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa em Python que irá calcular os
reajustes. Faça um programa que solicite ao usuário o salário de um colaborador e, em seguida,
calcule o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 2800,00 (incluindo): aumento de 20%
- salários entre R$ 2800,01 e R$ 7000,00 : aumento de 15%
- salários entre R$ 7000,01 e R$ 15000,00: aumento de 10%
- salários acima de R$ 15000,00: aumento de 5%
Após o aumento ser realizado, informe na tela o salário reajustado'''


#ENTRADA
salario_func = float(input("DIGITE O SALÁRIO DO FUNCIONÁRIO: R$ "))

#PROCESSAMENTO
if (salario_func <= 2800):
    salario_reajuste = salario_func * 1.20 #20% DE AUMENTO
elif (salario_func <= 7000):
    salario_reajuste = salario_func * 1.15 #15% DE AUMENTO
elif (salario_func <= 15000):
    salario_reajuste = salario_func * 1.10 #10% DE AUMENTO
else:
    salario_reajuste = salario_func * 1.05 #5% DE AUMENTO

#SAÍDA
print(f"O SALÁRIO REAJUSTADO É R$ {salario_reajuste:.2f}")