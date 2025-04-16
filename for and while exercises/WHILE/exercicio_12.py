'''12 · Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.
Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:

- média abaixo de 3.5 (reprovados direto)

- média entre 3,5 e 7 (exame)

- acima de 7 (aprovados)

Calcule a média aritmética da turma e informe o resultado no final.

E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.'''


#ENTRADA
soma_notas = 0
qtde_notas = 0
qtde_reprovados = 0
qtde_exame = 0
qtde_aprovados = 0

nota = float(input("DIGITE A NOTA DO ALUNO (NOTA NEGATIVA PARA SAIR): "))

#PROCESSAMENTO
while (nota >= 0):
    soma_notas += nota  #SOMA DAS NOTAS
    qtde_notas += 1
    if (nota < 3.5):
        qtde_reprovados += 1
    elif (nota <= 7.0):
        qtde_exame += 1
    else:
        qtde_aprovados += 1
    nota = float(input("DIGITE A NOTA DO ALUNO (NOTA NEGATIVA PARA SAIR): "))

media_turma = soma_notas / qtde_notas

#SAÍDA
print(f"A MÉDIA DA TURMA É {media_turma:.1f}.")
print(f"FORAM REPROVADOS {qtde_reprovados} ALUNOS.")
print(f"{qtde_exame} ALUNOS FORAM PARA EXAME.")
print(f"FORAM APROVADOS {qtde_aprovados} ALUNOS.")
