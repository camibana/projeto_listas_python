# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

nome = str(input('Digite o nome do Cliente:'))
print('Extrato bancário do cliente',nome)

nconta = int(input('Digite o número da conta:'))
saldo = float(input('Digite saldo da conta: R$ '))
vdebito = float(input('Digite o valor do débito na conta: R$ '))
vcredito = float(input('Digite o valor do crédito na conta: R$ '))
saldo_atual = saldo - vdebito + vcredito

if saldo_atual >= 0:
    print(f'R$ {saldo_atual} - Saldo Positivo')
else:
    print(f'R$ {saldo_atual} - Uso do cheque especial, Saldo Negativo')