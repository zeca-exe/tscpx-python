'''14 · Faça um programa que verifique se uma "senha”
numérica digitada pelo usuário está correta.
O programa deve repetir o pedido até que o
usuário escreva o valor correto. A senha correta deve estar definida no próprio programa.'''


senha_correta = 12345
senha_usuario = int(input("DIGITE SUA SENHA:"))


while (senha_usuario != senha_correta):
    senha_usuario = int(input("SENHA INVÁLIDA! DIGITE SUA SENHA NOVAMENTE:"))
print("SENHA CORRETA!")