''''15 · Desenvolva um programa que solicite ao usuário números positivos 
até que o valor 0 seja pressionado. Em seguida, calcule a média aritmética 
de todos os números recebidos (exceto o número 0). 
Além disso, apresente o maior e o menor número digitado.'''


#ENTRADA
soma = 0
qtde_numeros = 0

#PROCESSAMENTO
while True:
    num = int(input("DIGITE UM NÚMERO POSITIVO (OU 0 PARA ENCERRAR): "))  #ENTRADA
    if (num == 0):
        break  #FORÇA A SAÍDA DO WHILE
    elif (num > 0):
        soma += num
        qtde_numeros += 1
        if (qtde_numeros == 1):  #PRIMEIRO NÚMERO POSITIVO DIGITADO
            maior = num
            menor = num
        else:  #PRÓXIMOS NÚMEROS
            if (num > maior):
                maior = num
            if (num < menor):
                menor = num
    else:
        print("POR FAVOR, DIGITE APENAS NÚMEROS POSITIVOS!")

#PROCESSAMENTO
media = soma / qtde_numeros

#SAÍDA
print(f"A MÉDIA DOS NÚMEROS POSITIVOS É {media:.2f}.")
print(f"O MAIOR NÚMERO POSITIVO É {maior}.")
print(f"O MENOR NÚMERO POSITIVO É {menor}.")