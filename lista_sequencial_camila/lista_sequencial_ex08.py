# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
alt = float(input('Digite sua altura:'))
peso = (72.7 * alt) - 58
print('Para você que tem {:.2f} de altura, seu peso ideal é {:.2f}.'.format(alt, peso))