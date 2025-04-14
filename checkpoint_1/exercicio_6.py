'''Questão 6 [1,0 ponto] Pela tabela a seguir, mostre a descrição e o preço do produto após a
digitação do código pelo usuário. Se o produto não estiver cadastrado, emitir mensagem avisando.
Código Descrição Preço R$
01 Caneta 1.20
02 Lápis 0.80
03 Caderno 4.50
04 Borracha 1.00
05 Régua 1.50
OBS: é obrigatório utilizar a estrutura de decisão match...case'''

#ENTRADA
codigo_item = input("INFORME O CÓDIGO DO PRODUTO (01 - 05): ")

match codigo_item:
    case '01':
        print("CANETA | R$ 1,20 REAIS")
    case '02':
        print("LÁPIS | R$ 0,80 CENTAVOS")
    case '03':
        print("CADERNO | R$ 4,50 REAIS")
    case '04':
        print("BORRACHA | R$ 1,00 REAIS")
    case '05':
        print("RÉGUA | R$ 1,50 REAIS")
    case _:
        print("PRODUTO NÃO CADASTRADO!")

#PROCESSAMENTO
#SAÍDA