#Tratamento de erros no Python.


#Tratar o erro de conversão de tipos de dados.

#Simular um erro que pode acontecer.

numero = int(input("Digite um número: "))


#try...except...else...finally

# Exemplo: somar dois números inteiros.
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except ValueError: #o interpretador (Python) não conseguiu converter para int.
    print("Você deve digitar valores númericos!")
else: #o interpretador (Python) conseguiu converter para int
    soma = num1 + num2
    print(f"A soma dos números é: {soma}")
finally:#opcional.
    print("Operação finalizada.")