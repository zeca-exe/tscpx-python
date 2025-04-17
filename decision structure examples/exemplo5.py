'''Mostrar a modalidade do atleta de natação

- 5 a 12 anos: infantil
- 13 a 18 anos: juvenil
- 19 a 59 anos: adulto
 - 60 ou mais anos: senil
 obs: modalidades válidas de 5 a 90 anos'''

idade_pessoa= int(input("Digite a idade da pessoa:"))
'''
Operadores lógicos: 
- And (e): é verdadeiro se todas as condições forem verdade
- Or (ou):é verdadeiro se pelo menos uma condição for verdade
'''
if (idade_pessoa >= 5 and idade_pessoa <= 90):
    if (idade_pessoa <= 12):
        print("Modalidade Infantil")
    elif (idade_pessoa <= 18):
        print("Modalidade Juvenil")
    elif(idade_pessoa <= 59):
        print("Modalidade Adulto")
    else:
        print("Modalidade dos véio")
else:
    print("Idade Invalida")

