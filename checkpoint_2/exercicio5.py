'''
Faça um programa em Python que solicite ao usuário os seguintes dados
para 10 pessoas:
- nome
- idade
- gênero (masculino ou feminino)
- cor dos olhos

Ao final o exiba as seguintes informações:
a) o nome e a idade da pessoa mais velha;
b) o nome e a idade da pessoa mais jovem;
c) a quantidade de pessoas cuja idade está entre 18 e 35 anos (inclusive) e que tenham olhos
verdes.

OBS: é obrigatório utilizar a estrutura de repetição “for”. NÃO é permitido o uso de listas ou
qualquer outra estrutura de armazenamento de dados.
'''

olhos_verdes = 0

for cont in range(10):
    nome_pessoa = input("Digite o nome da pessoa: ")
    idade_pessoa = int(input("Digite a idade da pessoa: "))
    genero_pessoa = input("Digite o gênero da pessoa (F/M): ")
    cor_olhos = input("Digite a cor dos olhos da pessoa: ")
    if (idade_pessoa >= 18 and idade_pessoa <= 35 and cor_olhos == "verdes" and cor_olhos == "verde"):
        olhos_verdes+=1

    if (cont == 0):
        maior_idade = idade_pessoa
        nome_maior_idade = nome_pessoa
        menor_idade = idade_pessoa
        nome_menor_idade = nome_pessoa
    else:
        if (idade_pessoa > maior_idade):
            maior_idade = idade_pessoa
            nome_maior_idade = nome_pessoa
        if (idade_pessoa < menor_idade):
            menor_idade = idade_pessoa
            nome_menor_idade = nome_pessoa

print(f"Pessoa mais nova: {nome_menor_idade} | {menor_idade} anos")
print(f"Pessoa mais velha:{nome_maior_idade} | {maior_idade} anos")
print(f"Pessoas com idade entre 18-35 anos com olhos verdes: {olhos_verdes}.")