# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
tempc = float(input('Digite a temperatura em °C:'))
fahre = (tempc * 9 /5) + 32
print('Hoje está fazendo {:.1f} °F.'.format(fahre))