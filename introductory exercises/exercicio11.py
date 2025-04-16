'''
Escreva um programa que solicite a quilometragem parcial de um carro e a quantidade de litros gastos ele para percorrer esta quilometragem. Calcule quantos km/l o carro percorreu (autonomia) e exiba na tela.
'''
#ENTRADA
quilometragem = float(input("Digite a quilometragem percorrida de seu veículo (em km): "))
combustivel = float(input("Por favor, insira a quantidade de litros de combustível gastos: "))
#PROCESSAMENTO
kmpl = quilometragem / combustivel
#SAÍDA
print(f"Seu veículo percorreu {kmpl:.2f} km por litro")