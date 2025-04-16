'''
Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh), que deve ser uma variável real. O algoritmo deve, então, calcular o total da conta, considerando que cada kWh custa R$ 0,20.
'''
#ENTRADA
custo = 0.20
consumo = float(input("Por favor, insira o seu consumo de energia elétrica (em KWH): "))

#PROCESSAMENTO
total = consumo * custo

#SAÍDA
print(f"O total da sua conta de energia é de: R$ {total:.2f} reais.")