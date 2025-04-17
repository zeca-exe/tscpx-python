#Estrutura de Decisão - 3 ou mais situações (if...elif...else)

'''Exemplo: Quero mostrar se um número inteiro é positivo, negativo ou neutro.'''

num = int(input("Digite um número inteiro: "))

if (num > 0):
    print("O número é positivo!")
elif (num < 0):
    print ("O número é negativo!")
else:
    print ("O número é neutro!")