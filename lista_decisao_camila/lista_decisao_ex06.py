# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

v1 = float(input('Digite um valor:'))
v2 = float(input('Digite um valor:'))

while v1 != v2:
    if v1 < v2:
        print(f'Odrem crescente: {v1},{v2}')
    else:
         print(f'Odrem crescente: {v2},{v1}')
    break
while v1 == v2:
    print('Recomece e digite valores diferentes.')
    break