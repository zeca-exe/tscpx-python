'''O gerente de um bar precisa fazer um levantamento do movimento no final do expediente. Basicamente, o bar oferece um menu (tabela abaixo) onde cada item tem um código associado. Considerando que ele tem uma relação das comandas com as quantidades consumidas por mesa, escreva um programa em Python faça a leitura do código e da quantidade de cada item até que o usuário digite 0 (1-continuar e 0-parar). Calcule o total para cada comanda baseado nas quantidades de porções e cervejas consumidas e o valor total geral do dia. Para tanto, utilize a estrutura de repetição “while”.

Código Item Valor

01 Porção de fritas R$ 35,00

02 Porção de pastéis R$ 25,00

03 Tábua de frios R$ 40,00

04 Porção de peixes R$ 55,00

05 Cerveja R$ 18,00

'''

print("Bem-vindo ao sistema de levantamento do bar!")
print("Menu:")
print("Código | Item          | Valor")
print("01     | Porção de Fritas  | R$ 35,00")
print("02     | Porção de Pasteis | R$ 25,00")
print("03     | Tabua de frios    | R$ 40,00")
print("04     | Porção de Peixes  | R$ 55,00")
print("05     | Cerveja           | R$ 18,00")

resp= 1
total_dia= 0

while resp==1:
    codigo = int(input("Digite o código do produto:"))
    if (codigo >= 1 and codigo <=5):
        quantidade = int(input("Digite a quantidade:"))
        if quantidade > 0:
            match codigo:
                case 1:
                    total_dia+=quantidade * 35.00
                case 2:
                    total_dia += quantidade * 25.00
                case 3:
                    total_dia += quantidade * 40.00
                case 4:
                    total_dia += quantidade * 55.00
                case 5:
                    total_dia += quantidade * 18.00
        else:
            print("[ERRO]A quantidade deve ser maior do que zero! [ERRO]")
    else:
        print("[ERRO]CÓDIGO INVÁLIDO[ERRO]")
    resp = int(input("Deseja continuar? (1 - SIM / 0 - NÃO)"))

print(f"Total do dia foi de {total_dia:.2f} reais.")
