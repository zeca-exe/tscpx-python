'''
4. Foi feita uma estatística nas 4 cidades da região Sudeste do Brasil para
coletar dados sobre acidentes de trânsito no ano de 2023. Escreva um programa em Python que
solicite ao usuário os seguintes dados:
- nome da cidade.
- número de veículos de passeio.
- número de acidentes de trânsito com vítimas.

Ao final do programa, exiba:
a) qual o maior e o menor número de acidentes de trânsito e a que cidades pertencem
b) qual o maior e o menor número de veículos de passeio e a que cidades pertencem
c) qual a média de acidentes com vítimas da região Sudeste
OBS: é obrigatório utilizar a estrutura de repetição “for”. NÃO é permitido o uso de listas ou
qualquer outra estrutura de armazenamento de dados.
'''
soma_numero_acidentes = 0

for cont in range(4):
    nome_cidade = input("Digite o nome da cidade: ")
    numero_veiculos = int(input("Digite o numero de veículos de passeio dessa cidade: "))
    acidentes_vitimas = int(input("Digite o numero de acidentes de transito com vítimas dessa cidade: "))
    soma_numero_acidentes+=acidentes_vitimas
    if (cont == 0):
        maior_veiculos = numero_veiculos
        maior_acidentes = acidentes_vitimas
        cidade_maior_veiculos = nome_cidade
        cidade_maior_acidentes = nome_cidade
        menor_veiculos = numero_veiculos
        menor_acidentes = acidentes_vitimas
        cidade_menor_veiculos = nome_cidade
        cidade_menor_acidentes = nome_cidade
    else:
        if (numero_veiculos > maior_veiculos):
            maior_veiculos = numero_veiculos
            cidade_maior_veiculos = nome_cidade
        if (acidentes_vitimas > maior_acidentes):
            maior_acientes = acidentes_vitimas
            cidade_maior_acidentes = nome_cidade
        if (numero_veiculos < menor_veiculos):
            menor_veiculos = numero_veiculos
            cidade_menor_veiculos = nome_cidade
        if (acidentes_vitimas < menor_acidentes):
            menor_acidentes = acidentes_vitimas
            cidade_menor_acidentes = nome_cidade

print(f"Cidade com  menos veículos: {cidade_menor_veiculos} | {menor_veiculos} veículos.")
print(f"Cidade com menos acidentes com vítimas:{cidade_menor_acidentes} | {menor_acidentes} acidentes.")
print(f"Cidade com mais veículos: {cidade_maior_veiculos}| {maior_veiculos} veículos.")
print(f"Cidade com mais acidentes com vítimas:{cidade_maior_acidentes} | {maior_acidentes} acidentes.")

media_acidentes = soma_numero_acidentes / 4
print(f"A media de acidentes com vitimas é de {media_acidentes:.2f}%")