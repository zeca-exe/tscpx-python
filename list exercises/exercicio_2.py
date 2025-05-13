'''Desenvolva um programa que receba 10 números inteiros e os armazene em uma lista. Em seguida, o programa deve encontrar o maior elemento e exibir sua posição (índice) na lista.'''

lista_num = [] #Criar lista vazia

#Solicitar que o usuario informe 10 números para adicionar na lista_num

for i in range (10):
    num = int(input("Digite um número inteiro:"))
    lista_num.append(num)



# Encontrar o maior elemento da lista

maior = max(lista_num)


# Encontrar o índice que o maior elemento está armazenado
indice = lista_num.index(maior)

#Saída

print(f"O maior número da lista é: {maior}, e está armazenado no indíce: {indice}")