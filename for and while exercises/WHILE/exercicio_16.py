'''16 · O dono de uma mercearia da zona rural do interior de SP necessita automatizar o processo de totalização das compras de seus clientes, porém ele não tem condições financeiras para adquirir os equipamentos necessários para leitura de códigos de barras e afins. Dessa forma, o funcionário do caixa terá que digitar os preços dos produtos e as quantidades para que as compras dos clientes sejam totalizadas. Escreva um programa que calcule o total da compra do cliente, sendo que o usuário deverá digitar os preços e as quantidades dos produtos e, quando a compra terminar, digitar 0 (zero) no valor do preço para finalizar e informar o valor a pagar ao cliente.
'''



#ENTRADA
total_compra = 0

preco = float(input("INSIRA O PREÇO DO PRODUTO (0 PARA SAIR): "))  #ENTRADA

#PROCESSAMENTO
while (preco != 0):
    if (preco > 0):
        qtde_mercadoria = int(input("INSIRA A QUANTIDADE DE PRODUTOS: "))  #ENTRADA
        total_compra += qtde_mercadoria * preco
    else:
        print("O PREÇO DEVE SER UM VALOR MAIOR QUE ZERO.")
    preco = float(input("INSIRA O PREÇO DO PRODUTO (0 PARA SAIR): "))  #ENTRADA

#SAÍDA
print(f"O TOTAL DA COMPRA É DE R$ {total_compra:.2f}")