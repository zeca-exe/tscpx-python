'''
Escreva um programa que solicite 2 números inteiros p e q, faça a troca de seus valores e, no final, exiba p e q. (Exemplo: p=5 e q=7; após a troca: p=7 e q=5).
'''

#ENTRADA
p = int(input("Digite o valor de (P): "))
q = int(input("Digite o valor de (Q): "))


#PROCESSAMENTO
aux = p
p = q
q = aux

#SAÍDA
print(f"Os valores após a troca são: (P) = {p}, (Q) = {q}")

