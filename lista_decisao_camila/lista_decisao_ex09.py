# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nome = str(input('Digite o nome do Aluno:'))
print(f'Notas do aluno: {nome}')

n1 = float(input('Digite a 1ª nota:'))
n2 = float(input('Digite a 2ª nota:'))
print(f'A primeira nota foi {n1} e a segunda nota foi {n2}.')

media = (n1 + n2) / 2

#Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

if media >= 9:
    print(f'A média é {media}, conceito A - APROVADO')
elif media >= 7.5:
    print(f'A média é {media}, conceito B - APROVADO')
elif media >= 6:
    print(f'A média é {media}, conceito C - APROVADO')
elif media >= 4:
    print(f'A média é {media}, conceito D - REPROVADO')
else:
    print(f'A média é {media}, conceito E - REPROVADO')
