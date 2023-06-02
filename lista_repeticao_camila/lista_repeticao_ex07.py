# Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.
print('Cadastre-se abaixo:')
nome = []
idade = []
email = []
limite = int(input('Quantas pessoas você quer incluir neste cadastro?'))

for n in range(limite):
    n = str(input('Insira seu nome completo:'))
    
    nome.append(n)
    print(f'Nome Completo:{nome}')

for i in range(limite):
    i = int(input('Insira sua idade:'))
    idade.append(i)
    print(f'Idade:{idade}')

for e in range(limite):
    e = str(input('Insira seu e-mail:'))
    email.append(e)
    print(f'E-mail: {email}')