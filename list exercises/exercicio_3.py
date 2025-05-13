'''Desenvolva um programa que preencha um vetor com as idades dos usuários até que o usuário digite um valor negativo, o valor negativo não deve ser inserido na lista. Ao final, exiba na tela:

- A quantidade de usuários menores de 18 anos;

- A média das idades.'''

lista_idade = []


qtde_menores = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    if (idade <0):
        break
    lista_idade.append (idade)


#Percorrer a lista_idade para contar os menores de 18 anos.

tamanho_lista = len(lista_idade)

for i in range (tamanho_lista):
    if (lista_idade[i] < 18):
        qtde_menores+=1
media = sum(lista_idade) / tamanho_lista

#Saída

print(f"{qtde_menores} pessoas tem menos que 18 anos.")
print(f"A média das idades é: {media:.2f}")

