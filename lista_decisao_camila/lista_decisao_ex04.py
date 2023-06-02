# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nome = str(input('Digite o nome do Aluno:'))
print(f'Notas do aluno: {nome}')
n1 = float(input('Digite a nota da 1ª avaliação:'))
n2 = float(input('Digite a nota da 2ª avaliação:'))
print(f'Suas notas foram {n1} e {n2}.')
media = (n1 + n2) / 2
if media >= 6:
    print(f'O(a) aluno(a) {nome} teve média {media} e foi aprovado(a)!')
else:
    print(f'O(a) aluno(a) {nome} teve média {media} e não foi aprovado(a)!')