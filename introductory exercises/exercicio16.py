'''
Escreva um algoritmo para solicite o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
'''

#ENTRADA
print("Bem-vindo ao Sistema de Análise Eleitoral!")
print("Aqui, você pode inserir os dados da eleição e obter os percentuais de votos brancos, nulos e válidos.\n")
vb = int(input("Primeiramente, insira o número de votos brancos: ")) #vb = votos em branco
vn = int(input("Em seguida, o número de votos nulos: ")) #vn = votos nulos
vv = int(input("E por fim, o número de votos válidos: ")) #vv = votos validos

te = vb + vn + vv #te=total de eleitores
# PROCESSAMENTO - pb = percentual branco - pn = percentual nulos - pv=percentual validos
pb = (vb / te) * 100
pn = (vn / te) * 100
pv = (vv / te) * 100

#SAÍDA

print("Resultados da Eleição:")
print(f"Total de eleitores: {te}")
print(f"Votos brancos: {vb} ({pb:.2f}%)")
print(f"Votos nulos: {vn} ({pn:.2f}%)")
print(f"Votos válidos: {vv} ({pv:.2f}%)")
print("Obrigado por usar o Sistema de Análise Eleitoral!")