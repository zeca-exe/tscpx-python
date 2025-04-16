'''Faça um algoritmo que solicite ao usuário a idade de uma pessoa expressa em anos, meses e dias 
e escreva a idade dessa pessoa expressa apenas em dias. 
Considerar ano com 365 dias e mês com 30 dias. Por fim, exiba a idade da pessoa expressa apenas em dias.'''

#ied = idade em dias

#Entrada
anos = int(input("Digite uma idade em anos: "))
meses = int(input("Digite uma idade em meses: "))
dias = int(input("Digite uma idade em dias: "))

#Processamento
ied = (anos * 365) + (meses * 30) + dias

#Saída
print(f"A idade em dias é: {ied} dias")