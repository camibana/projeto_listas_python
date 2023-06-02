# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite um número inteiro:'))
n3 = float(input('Digite um número real:'))

# 1. o produto do dobro do primeiro com metade do segundo .

calc1 = n1 * 2 * n2 / 2
print(calc1)

# 2. a soma do triplo do primeiro com o terceiro.
calc2 = n1 * 3 + n3
print(calc2)

# 3. o terceiro elevado ao cubo.

calc3 = n3 ** 3
print('{:.2f}'.format(calc3))
