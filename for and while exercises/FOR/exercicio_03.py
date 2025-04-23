'''3. A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Escreva um programa em Python para coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:

a) Média de salário da população

b) Média do número de filhos

c) Maior salário dos habitantes

d) Percentual de pessoas com salário menor que R$ 150,00

Obs.: O final das leituras dos dados se dará com a entrada de um “salário negativo”. Utilize a estrutura de repetição “while”.'''

th = 0 #TOTAL DE HABITANTES
ts = 0.0 #TOTAL SALARIO
tf = 0 #TOTAL FILHOs
maior_salario = 0.0
abaixo = 0 #ABAIXO DOS 150 REAIS

#ENTRADA
print("PESQUISA DA PREFEITURA DE DEEPWATER (PARA ENCERRAR DIGITE UM SALÁRIO NEGATIVO)")
while True:
    salario = float(input("Digite o salário do habitante: R$ "))
    if salario < 0:
        break
#PROCESSAMENTO
    filhos = int(input("Digite o número de filhos: "))
    if filhos < 0:
        break
    th += 1
    ts += salario
    tf += filhos
    if salario > maior_salario:
        maior_salario = salario
    if salario < 150.00:
        abaixo += 1
if th > 0:
    media_salario = ts / th
    media_filhos = tf / th
    percentual = (abaixo / th) * 100
else:
    media_salario = 0
    media_filhos = 0
    percentual = 0
    maior_salario = 0

#SAIDA
print("Resultados da Pesquisa:")
print(f"A) Média de salário da população: R$ {media_salario:.2f}")
print(f"B) Média do número de filhos: {media_filhos:.1f}")
print(f"C) Maior salário dos habitantes: R$ {maior_salario:.2f}")
print(f"D) Percentual de pessoas com salário menor que R$ 150,00: {percentual:.1f}%")