'''
Um estacionamento cobra R$ 5,00 por hora. Escreva um algoritmo que pergunte ao usuário qual foi o período de permanência em horas e calcule o total a pagar.
'''
#ENTRADA
tempo = float(input("Por favor, digita o período de sua permanência no estacionamento (em horas): "))

#PROCESSAMENTO
vph = 5.00 #vph = valor por hora
total = tempo * vph

#SAÍDA
print(f"O valor total a ser pago é de: R$ {total:.2f} reais")