'''
3. Foi feita uma pesquisa entre um grupo de habitantes de uma região. Foram
coletados os dados do nome, idade, sexo (M/F) e salário. Nesse sentido, escreva um programa que
solicite esses dados ao usuário e que encerre as entradas quando for digitada uma idade negativa.
Ao final, exiba:
a) a média de salário das mulheres;
b) maior e menor idade do grupo, bem como os respectivos nomes;
c) quantidade de homens com salário até R$10000.
OBS: é obrigatório utilizar a estrutura de repetição “while”. NÃO é permitido o uso de listas ou
qualquer outra estrutura de armazenamento de dados
'''

soma_salarios_mulheres = 0
mulheres = 0
salario_homens = 0
habitantes = 0

idade = int(input("Digite a idade do habitante [VALOR NEGATIVO PARA SAIR]: "))

while (idade >= 0):
    habitantes+=1
    nome = input("Digite o nome do habitante: ")
    sexo = input("Digite o gênero do habitante (M/F): ")
    salario = float(input("Digite o salário do habitante: "))
    if (sexo == "F"):
        soma_salarios_mulheres+=salario
        mulheres+=1
    if (sexo == "M" and salario <= 10000):
        salario_homens+=1
    if (habitantes == 1):
        maior_idade = idade
        menor_idade = idade
        nome_maior_idade = nome
        nome_menor_idade = nome
    else:
        if (idade > maior_idade):
            maior_idade = idade
            nome_maior_idade = nome
        if (idade < menor_idade):
            menor_idade = idade
            nome_menor_idade = nome

    idade = int(input("Digite a idade do habitante [VALOR NEGATIVO PARA SAIR]: "))

media_salarial_mulheres = soma_salarios_mulheres / mulheres
print(f"A média salarial das habitantes mulheres é de R$ {media_salarial_mulheres:.2f} reais.")

print(f"Habitante mais novo: {nome_menor_idade} | {menor_idade} anos.")
print(f"Habitante mais velho: {nome_maior_idade} | {maior_idade} anos.")

print(f"Quantidade de habitantes homens com salário até R$10.000,00: {salario_homens}.")