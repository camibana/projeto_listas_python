# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

v1 = float(input('Digite um valor:'))
v2 = float(input('Digite um valor:'))

while v1 != v2:
    if v1 > v2:
        print(f'O primeiro valor digitado, {v1} é o maior.')
    else:
        print(f'O segundo valor digitado, {v2} é o maior.')
    break
while v1 == v2:
    print('Recomece e digite valores diferentes.')
    break