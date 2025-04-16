'''1· O jogo do PIM era uma brincadeira conthecida do Silvio Santos em 
seu programa de auditório que contsistia em pedir a alguém que recite 
uma sequência numérica iniciada em 1 e caso o número seja múltiplo de quatro 
deveria substitui-lo pela palavra PIM. Faça um programa que escreva na tela 
uma sequência de 1 a 30 substituindo os múltiplos de quatro pela palavra PIM.'''

for cont in range (1,31): #ENTRADA #O CONT VAI VARIAR DE 1 ATÉ 30
    if (cont % 4 == 0): #PROCESSAMENTO E SAÍDA
        print(f"PLIM!")
    else:
        print(f"{cont}")