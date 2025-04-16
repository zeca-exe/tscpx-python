'''Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, 
mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. 
Escrever um algoritmo que solicite ao usuário o número de carros por ele vendidos, o valor total de suas vendas, 
o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.'''
#ENTRADA
salario = float(input("Digite o salário fixo do vendedor: R$ "))
comissao = float(input("Digite o valor da comissão por carro vendido: R$ "))
tdcv = int(input("Digite o número de carros vendidos: ")) #tdvc=total de carros vendidos
vt = float(input("Digite o valor total das vendas: R$ ")) #vt=venda total


#PROCESSAMENTO
cc = tdcv * comissao #cc= comissao de carros
cv = vt * 0.05 #cv = comissao de vendas
salario_final = salario + cc + cv

#SAÍDA
print(f"O salário final do vendedor é de: R$ {salario_final:.2f} reais")