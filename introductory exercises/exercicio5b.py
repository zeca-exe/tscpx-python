''''Escreva um programa que solicite o valor da cotação do dólar (em reais) do dia, 
faça a conversão de um valor em dólares para reais. EM seguida, exiba o valor que foi convertido para reais.'''



#Entrada

cotacao = float(input("Insira a cotação do Dólar (em reais) hoje: R$ "))
dolares = float(input("Digite o valor em Dólares que deseja converter: $ "))
#Processamento

reais = dolares * cotacao
#Saída
print(f"Com base na cotação de hoje, o valor de $ {dolares:.2f} dólares equivale a R$ {reais:.2f} reais.")
