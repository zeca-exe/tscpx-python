'''Questão 1 [2,5 pontos] O salário de um professor é calculado considerando 3 itens: o salário base,
a hora-atividade e o DSR (descanso semanal remunerado). O salário base é calculado a partir da
multiplicação do número de aulas semanais por 4,5 semanas no mês e pelo valor da hora/aula. A
hora-atividade é calculada como um adicional de 5% do salário base (preparação de atividades,
correção de provas, etc). Já o DSR é calculado como 1/6 do sálario base junto com o valor da horaatividade. O salário final é calculado como a soma do salário base com a hora-atividade e o DSR.
Nesse contexto, crie um programa em Python que solicite ao usuário o valor da hora/aula e o
número de aulas semanais. Por fim, calcule e mostre o salário final do professor.
'''

#ENTRADA
valor_hora_aula = float(input("DIGITE O VALOR DA HORA/AULA: R$ "))
numero_aulas = int(input("DIGITE O NÚMERO DE AULAS SEMANAIS: "))

#PROCESSAMENTO
salario_base = numero_aulas * 4.5 * valor_hora_aula #MÉDIA DE 4,5 SEMANAS POR MÊS
hora_atividade = salario_base * 0.05 #5% DE HORA ATIVIDADE
dsr = (salario_base + hora_atividade) / 6 #DSR=DESCANSO SEMANAL REMUNERADO

salario_final = salario_base + hora_atividade + dsr

#SAÍDA
print(f"O SALÁRIO FINAL DO PROFESSOR É R$ {salario_final:.2f}")