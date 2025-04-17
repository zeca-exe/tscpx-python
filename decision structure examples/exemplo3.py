#Mostrar se um número inteiro é par ou ímpar.

num = int(input("Digite um número inteiro: "))

resto_div= num % 2

if (resto_div == 0):
    print ("O número é par")

else:
    print ("O número é ímpar")