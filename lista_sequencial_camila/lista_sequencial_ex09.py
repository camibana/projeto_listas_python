# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
print('Descubra hoje seu peso ideal!')
nome = str(input('Identifique-se:'))
alt = float(input('Digite sua altura:'))
sexo = str(input('Digite H se você é Homem e M se você é mulher:'))

# 1. Para homens: (72.7*h) - 58
# 2. Para mulheres: (62.1*h) - 44.7

if sexo == 'H':
    pesoh = (72.7 * alt) - 58
    print('Olá {}, já que você é homem, e sua altura é {:.2f}, seu peso ideal é {:.2f}.'.format(nome, alt, pesoh))
else:
    pesom = (62.1 * alt) - 44.7
    print('Olá {}, já que você é mulher, e sua altura é {:.2f}, seu peso ideal é {:.2f}.'.format(nome, alt, pesom))