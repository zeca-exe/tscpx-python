'''Faça um algoritmo que solicite ao usuário a idade de uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa apenas em dias. 
Considerar ano com 365 dias e mês com 30 dias. Por fim, exiba a idade da pessoa expressa apenas em dias.'''


#iea = idade em anos, iem = idade em meses, ied = idade em dias
#Entrada
iea = int(input("Por favor, digite sua idade em anos: "))

#Processamento
iem = iea * 12  
ied = iea * 365

#Saída
print(f"A sua idade de {iea} anos equivale a:")
print(f"- {iem} meses")
print(f"- {ied} dias")