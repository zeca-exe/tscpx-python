#Tratar o erro da divisão de um número por zero.

# Simular o erro:

#div= 5 / 0


#Exemplo: dividir dois números digitados pelo usuário.
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    divisao = num1 / num2
except ValueError:  # o interpretador (Python) não conseguiu converter para int.
    print("Você deve digitar valores númericos!")
except ZeroDivisionError:
    print("Não ÉCSISTE divisão por zero!")
else:
    print((f"Divisão dos números: {div:.2f}"))
finally:#opcional
    print("Operação finalizada.")