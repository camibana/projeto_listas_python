# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.
produto = str(input('Digite nome do produto:'))
print('Estoque do produto', produto)

qatual = float(input('Insira a quantidade atual do estoque:'))
qmaxima = float(input('Insira a quantidade máxima do estoque:'))
qminima = float(input('Insira a quantidade mínima do estoque:'))

qmedia = (qmaxima + qminima) / 2

if qatual >= qmedia:
    print(f'A quantidade atual em estoque é de:{qatual}, sendo maior que a quantidade média {qmedia}')
    print('Não efetuar compra')
else:
     print(f'A quantidade atual em estoque é de:{qatual}, sendo menor que a quantidade média {qmedia}')
     print('Efetuar compra')