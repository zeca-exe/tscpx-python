'''Construa um programa que solicite ao usuário os valores das compras de cinco clientes de uma loja. Ao final, o programa deverá exibir:

(a) o valor total pago pelos cinco clientes;

(b) o valor da compra média efetuada;

(c) o número de clientes que efetuaram compras superiores a 100 reais;

(d) quantos clientes efetuaram compras inferiores a 50 reais.

OBS: é obrigatório utilizar a estrutura de repetição “for”.'''


valor_total=0
compras_acima = 0
compras_abaixo = 0

for cont in range (5):
    valor_compra = float(input("Digite o valor da compra do cliente: "))
    if (valor_compra > 0):
        valor_total+=valor_compra
        if (valor_compra > 100):
            compras_acima+=1
        if (valor_compra < 50):
            compras_abaixo += 1
    else:
        print("O valor da compra deve ser maior do que R$ 0,00 Reais.")

print (f"O valor total das compras é R$ {valor_total:.2f}")

media_valor = valor_total / 5

print (f"A média dos valores das compras é de R$ {media_valor} reais.")
print (f"{compras_acima} clientes compraram acima de R$ 100,00 reais.")
print (f"{compras_abaixo} clientes compraram acima de R$ 50,00 reais.")