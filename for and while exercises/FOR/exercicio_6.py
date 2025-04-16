'''6· Ler um valor N e imprimir todos os valores inteiros
entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO.'''

#ENTRADA
num = int(input("DIGITE UM VALOR (MAIOR QUE 0): "))
#PROCESSAMENTO/SAÍDA
if (num > 0):
    print(f"VALORES INTEIROS ENTRE 1 e {num} SÃO:")
    for cont in range(1, num + 1):
        print(cont)
else:
    print(f"O VALOR DEVE SER MAIOR QUE ZERO.")