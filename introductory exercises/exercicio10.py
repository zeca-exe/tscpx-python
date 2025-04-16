'''Escreva um algoritmo para calcular a média aritmética de
 3 avaliações que deverão ser informadas. Por fim, exiba o valor da média'''

#ENTRADA
aluno = input("Olá, bem-vindo ao sistema de calculo de média de avaliações. Por favor, primeiramente insira o nome do aluno: ")
nota1 = float(input("Agora, digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
#PROCESSAMENTO
media = (nota1 + nota2 + nota3) / 3

#SAÍDA
print(f"A média das três avaliações do aluno {aluno} é: {media:.2f}")