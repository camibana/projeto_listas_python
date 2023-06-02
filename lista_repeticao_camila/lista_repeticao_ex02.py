#Faça um programa que mostre as tabuadas dos números de 1 a 10.

for n in range(1,11):
    print('Tabuada do {}:'.format(n))
    for num in range(1,11):
        print('{} * {}  = {}'.format(n, num, n * num))
    print('-' * 10)
