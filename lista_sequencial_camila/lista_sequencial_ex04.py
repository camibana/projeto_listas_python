# # Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
nome = str(input('Insira seu nome:'))
hvalor = float(input('Insira o valor da sua hora de trabalho:'))
hnum = float(input('Insira quantas horas você trabalhou esse mês:'))
salario = hnum * hvalor
print('{} trabalhou {:.2f} horas por R$ {:.2f}, sendo assim receberá R$ {:.2f}.'.format(nome, hnum, hvalor, salario))