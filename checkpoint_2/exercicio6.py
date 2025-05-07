'''
6. Faça um programa em Python que solicite as idades de pessoas até que
uma idade negativa seja digitada. Ao final, o programa deverá verificar se a média de idade da turma
varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
respectivamente, conforme a média calculada.

OBS: é obrigatório utilizar a estrutura de repetição “while”. NÃO é permitido o uso de listas ou
qualquer outra estrutura de armazenamento de dados.
'''
soma_idades = 0
pessoas = 0

while True:
    idade = int(input("Digite a idade da pessoa [VALOR NEGATIVO PARA SAIR]: "))
    if (idade < 0):
        break
    soma_idades+=idade
    pessoas+=1

media_idades = soma_idades / pessoas

if (media_idades >= 0 and media_idades <= 25):
    print("[A TURMA É JOVEM]")
elif (media_idades <= 60):
    print("[A TURMA É ADULTA]")
else:
    print("[A TURMA É IDOSA]")
