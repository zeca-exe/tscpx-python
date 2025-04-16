'''4· Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.'''

soma = 0


for cont in range(10):
    num = int(input(f"DIGITE O {cont + 1}º NÚMERO INTEIRO: ")) #ENTRADA
    if (num < 40): #PROCESSAMENTO
        soma = num + soma

print(f"OS VALORES MENORES DO QUE 40 FORAM SOMADOS! O RESULTADO É: {soma}") #SAÍDA