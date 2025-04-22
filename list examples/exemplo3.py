#Funções para inserir e remover elementos de uma lista
lista_num = [1, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14,15, 100]
#Função de inserção (append)
lista_num.append(25)

print(lista_num)

#ORDENANDO ORDEM CRESCENTE[
lista_ord_crescente = sorted(lista_num)

print (f"Lista em ordem crescente: {lista_ord_crescente}")
#]

#Função de inserção (insert)

lista_num.insert(2,35)
print(lista_num)

#Função de remoção (pop)

lista_num.pop() #Remove o último elemento da lista
print(lista_num)

lista_num.pop(1)#Remove o SEGUNDO elemento da lista
print(lista_num)

