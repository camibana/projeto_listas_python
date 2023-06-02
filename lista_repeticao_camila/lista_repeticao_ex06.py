# Seja criativo ao desenvolver este programa.
# a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

conv = ['Taylor Swift', 'Avril Lavigne', 'Humberto Gessinger', 'Bruno Gouvêia', 'Manu Gavassi']

# b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
for n in conv:
    print(f'Olá querido(a) {n}! É com imenso prazer que o convido para a noite mais especial do ano: meu jantar anual beneficente! Sua presença é indispensável!')
    print('\n')

# c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
print(f'As celebridades {conv[2]} e {conv[4]} não poderão está presente.')

# d. Modifique sua lista, substitua os desistentes por novos convidados.
conv[2] = 'Nando Reis'
conv[4] = 'Lady Gaga'
print(conv)

# e. Exiba um novo convite para cada pessoa que continua presente em sua lista.
for n in conv:
    print(f'Olá querido(a) {n}! É com imenso prazer que o convido para a noite mais especial do ano: meu jantar anual beneficente! Sua presença é indispensável!')
    print('\n')