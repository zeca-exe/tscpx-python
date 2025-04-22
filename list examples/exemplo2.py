#FUNÇÕES MAIS UTILIZADAS EM LISTAS

lista_num = [1, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14,15, 100]

#FUNÇÃO QUE RETORNA O TAMANHO DA LISTA

tamanho = len (lista_num)

print (f"A lista tem {tamanho} elementos")


#função que retorna o maior e menor elemento da lista

maior = max (lista_num)
menor = min (lista_num)

print (f"O MAIOR NÚMERO É {maior} e o MENOR É {menor}")

#função que calcula o somatorio da lista


soma = sum(lista_num)
print (f"A soma dos elementos da lista é {soma}")


#Função que faz a ordenação da lista

lista_ord_crescente = sorted(lista_num)

print (f"Lista em ordem crescente: {lista_ord_crescente}")

lista_ord_decrescente = sorted(lista_num, reverse=True)

print (f"Lista em ordem decrescente: {lista_ord_decrescente}")

#Verificar se um elemento pertence a lista

elemento = int(input("Digite um elemento que gostaria de procurar na lista: "))

if elemento in lista_num: #Se isso for TRUE [verdadeiro]
    print(f"O elemento {elemento} consta na lista")
else:
    print(f"O elemento {elemento} não consta na lista")

#Função que retorna o indice de um elemento na lista

if elemento in lista_num:
    indice = lista_num.index(elemento)
    print(f"{elemento} está armazenado no índice {indice}")