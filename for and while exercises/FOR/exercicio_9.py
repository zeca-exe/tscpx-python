'''9· Escreva um programa para calcular o fatorial de um número n digitado 
pelo usuário. 
Por exemplo: n = 5 fatorial = 5 x 4 x 3 x 2 x 1 = 120. OBS: utilize o “for”.'''

#ENTRADA
num = int(input("DIGITE UM NUMERO INTEIRO PARA INICIARMOS NOSSO CALCULO FATORIAL: "))

#PROCESSAMENTO
if num < 0:
    print("VALOR INVÁLIDO.")

else:
    fatorial = 1
    
    for cont in range(1, num + 1):
        fatorial *= cont
#SAÍDA  
    print(f"O fatorial de {num} é {fatorial}")