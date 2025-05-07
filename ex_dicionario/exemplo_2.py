'''CRIAR E EXIBIR UMA LISTA DE DICIONÁRIO PARA ARMAZENAR DADOS PARA 5 ALUNOS.'''

import pandas as pd

lista_alunos = [] #Criando uma lista vazia

for i in range(5):
    rm=int(input("Digite o RM do aluno: "))
    nome = (input("Digite o nome do aluno: "))
    curso = (input("Digite o curso do aluno: "))
    media_geral = float(input("Digite a média do aluno: "))
    aluno = {
        'RM':rm,
        'Nome':nome,
        'Curso':curso,
        'Media_geral':media_geral
    }
    lista_alunos.append(aluno)

#Exibir todos os alunos da lista
for i in range(5):
    for chave, valor in lista_alunos[i].items():
        print(f"{chave}: {valor}")
    print("▬▬▬▬▬▬▬▬▬")

#BONUS: criar um Dataframe pela lista de alunos

df_alunos = pd.DataFrame(lista_alunos)

print(df_alunos)