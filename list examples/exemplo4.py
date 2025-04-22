#Solicitar que o usuário digite 10 números inteiros para criar uma lista

#Criando uma lista vazia para o usuario inserir elementos
lista = []

for i in range (10):
    num = int(input("Digite um elemento para inserir na lista:"))
    lista.append(num)
print(lista)
#Exibir os elementos da lista um de baixo do outro
#Primeira forma:
for i in range (10):
    print (lista [i])

#Segunda forma:
for elemento in lista:
    print(elemento)