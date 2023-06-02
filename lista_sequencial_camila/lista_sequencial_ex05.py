# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
tempf = float(input('Digite a temperatura em °F:'))
celsius = 5 * ((tempf-32) / 9 )
print('Hoje está fazendo {:.1f} °C.'.format(celsius))