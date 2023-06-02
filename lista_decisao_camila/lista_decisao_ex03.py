# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

quantidade = int(input('Digite quantas maçãs serão compradas?'))

if quantidade >= 12:
    print('Levando a partir de 12 unidades, as maçãs custam R$ 1.00')
    print('Ja que você vai levar {} maças, o valor total de sua compra será R$ {}'.format(quantidade, (quantidade * 1)))
else:
    print('Levando menos que de 12 unidades, as maçãs custam R$ 1.30')
    print('Ja que você vai levar {} maças, o valor total de sua compra será R$ {}'.format(quantidade, (quantidade * 1.30)))