# Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

num = int(input('Digite o nº aqui:'))
print('A tabuada do número: {}'.format(num))
print('\n')
   
for x in range(1, 11):
    print('{} x {} = {}'.format(num, x, (num * x)))
