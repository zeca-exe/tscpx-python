'''Escreva um programa em Python que crie uma lista de 10 alunos, utilizando o conceito de dicionários, contendo os seguintes dados:

o Nome;

o Curso;

o Disciplina;

o Faltas;

o 3 checkpoints.

Depois da lista criada, exiba todos os funcionários com seus dados um debaixo do outro.

OBS: o programa deverá solicitar que o usuário informe os dados para alimentar a lista de dicionários.'''


lista_aluno = []


for i in range(10):
    try:
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        disciplina = input("Digite o disciplina do aluno: ")
        faltas = int(input("Digite a quantidade de faltas: "))
        lista_cp = []
        for cont in range (3):
            cp = float(input(f"Digite a nota do [CP {cont+1}]: "))
            lista_cp.append(cp)
    except ValueError: #Erro de conversão de dados
        print ("A quantidade de faltas e os checkpoints devem ser numéricos")
    else: #Dados Ok
        aluno = {
            'Nome':nome, 'Curso':curso,'Disciplina':disciplina,'Faltas':faltas,'Checkpoints':lista_cp
        }

        lista_aluno.append(aluno)
    finally:
        print ("Operação finalizada!")


#Saída
for aluno in lista_aluno:
    for chave,valor in aluno.items():
        print (f"{chave}: {valor}")
    print (f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
