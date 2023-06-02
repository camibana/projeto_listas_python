# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi
raio = float(input('Insira o tamanho do raio do círculo:'))
area = pi * (raio ** 2)
print('Para um círculo de tamanho {:.2f}, a sua area é de {:.2f}.'.format(raio, area))