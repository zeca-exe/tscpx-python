'''Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista.
Em seguida, armazene os números pares na lista PAR e os números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas'''


lista_num = [] #Criar lista vazia
lista_pares = []
lista_impares = []

#Solicitar que o usuario informe 10 números para adicionar na lista_num

for i in range (10):
    num = int(input("Digite um número inteiro:"))
    lista_num.append(num)


#Percorrer a lista_num para adicionar os pares e impares

for i in range(10):
    if (lista_num[i] % 2 == 0):
        lista_pares.append(lista_num[i])
    else:
        lista_impares.append(lista_num[i])

#Saída.
print(f"Lista dos 10 números: {lista_num}")
print(f"Lista dos números pares: {lista_pares}")
print(f"Lista dos números impares: {lista_impares}")