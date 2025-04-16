'''3· Desenvolva um programa que receba:

- taxa de abatimento em porcentagem;

- número de prestações;

- valor da primeira prestação.

Seu programa deverá exibir na tela os valores das prestações na forma decrescente, dado que a cada mês o valor da prestação diminui do valor da prestação do mês anterior (utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo). OBS: utilize o “for”.
 '''


# ENTRADA
taxa_abatimento = float(input("POR FAVOR, INSIRA A TAXA(%) DE ABATIMENTO: "))
num_prest = int(input("QUAL O NÚMERO DE PRESTAÇÕES? "))
valor_1prest = float(input("INSIRA O VALOR DA PRIMEIRA PRESTAÇÃO: "))

valor_prest = valor_1prest

# PROCESSAMENTO E SAÍDA
print("\nVALOR DAS PRESTAÇÕES:")
for cont in range(1,num_prest+1):
    print(f"PRESTAÇÃO {cont}: R$ {valor_prest:.2f}")
    valor_prest = valor_prest - (valor_prest * taxa_abatimento / 100)

