'''Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas. Para tanto, crie uma lista para as palavras em inglês e outra para as traduções em português nas respectivas posições. A inserção das palavras deverá ser executada até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). Após a inserção, exiba a tradução em português de uma determinada palavra em inglês que o usuário deverá digitar..'''

#Listas de idiomas vazias.
pt = []
eng = []


resp = 1

while (resp == 1):
    word = input ("Digite a palavra em inglês: ")
    eng.append(word)
    palavra = input("Digite a tradução em português: ")
    pt.append(palavra)
    resp = int(input("Deseja continuar? [1-SIM/ 0-NÃO]"))

# Exibir tradução:

user_word = input("Digite a palavra em inglês que deseja saber a tradução em português.")

if (user_word in eng):
    indice = eng.index(user_word)
    print (f"A tradução da palavra é: {pt[indice]}")
