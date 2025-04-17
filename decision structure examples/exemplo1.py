#Estruturas de Decisão no Python

# 2 Situações (IF... ELSE)
#Entrada
aluno = input("Olá, bem-vindo ao sistema de calculo de média de avaliações. Por favor, primeiramente insira o nome do aluno: ")
nota1 = float(input("Agora, digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

#Processamento
media = (nota1 + nota2 + nota3) / 3


#Saída
print(f"A média final do aluno foi de {media:.1f}, por tanto...")

if (media >= 7.0):
    print("o aluno foi aprovado!")
else:
    print("o aluno foi reprovado :(")
