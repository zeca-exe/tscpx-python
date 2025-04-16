''''Escreva um programa que solicite o valor da cotação do dólar (em reais) do dia, 
faça a conversão de um valor em dólares para reais. EM seguida, exiba o valor que foi convertido para reais.'''



#Entrada

valor_real = float (input("Insira o valor em Dólares que será convertido em Reais: $ "))
valor_dolar = valor_real * 5.74
#Processamento

valor_dolar = valor_real * 5.74
#Saída
print(f"Com base na cotação do dia 15 de Março de 2025 ($ 1,00 = R$ 5,74), o valor convertido é de: R$ {valor_dolar:.2f}")