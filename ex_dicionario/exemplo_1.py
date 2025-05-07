# Dicionário em Python.


# Criação de um dicionário para armazenar dados de um aluno:

aluno = {'RM':563051, 'Nome':"Zeca", 'Curso':"TSC", 'Media_geral':8.5}
#item:'chave':valor

# Forma mais simples de exibir um dicionário:

print(aluno)

# Exibir o curso do aluno:

print(f"Curso do aluno: {aluno['Curso']}")


# Exibir os nomes das chaves do dicionário:
print(aluno.keys())
# Exibir os valores das chaves:
print(aluno.values())

# Exibir os itens do dicionário separadamente (um de baixo do outro)

# Método items(): Retorna os itens do dicionário em formato de tuplas(chave,valor):
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

