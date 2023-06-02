# Construindo um jogo da Forca
import random
import os
import time

temas = {
    'cidades': ['salvador', 'recife', 'manaus'],
    'objetos': ['caneta', 'cinto', 'toalha'],
    'sobremesas': ['pudim', 'bolo', 'sorvete'],
    'animais': ['baleia', 'cachorro', 'girafa']
}


def limpar_tela():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def jogar_novamente():
    while True:
        resposta = input(
            "\nDeseja jogar novamente? ('S' para sim / 'N' para não): ").lower()
        if resposta == "s" or resposta == "n":
            return resposta == "s"
        else:
            print("Entrada inválida. Digite 'S' para sim ou 'N' para não.")


def jogar_forca():
    print('Vamos iniciar seu jogo da forca!')
    print('\n')
    print('Funciona assim: Com base em um dos temas disponíveis, você vai receber uma palavra secreta e tentar acertar as letras \nque a compõe antes de errar a ponto de ficar enforcado!')
    print('\n')
    print('Are ready for it? Have fun and enjoy the game!')
    print('\n')

    inicio = input(
        'Se você deseja escolher seu tema digite E, se podemos escolher o tema aleatoriamente digite A: ').upper()
    while inicio not in ['A', 'E']:
        inicio = input(
            'Entrada inválida. Digite "A" para tema aleatório ou "E" para escolher um tema: ').upper()

    if inicio == 'A':
        tema_escolhido = random.choice(list(temas.keys()))
        print(f'O tema escolhido aleatoriamente é: {tema_escolhido}')
        palavra = random.choice(temas[tema_escolhido])
    else:
        print(list(temas.keys()))
        tema_escolhido = input(
            'Escolha o tema pelo número correspondente (1-Cidades, 2-Objetos, 3-Sobremesas, 4-Animais): ')
        while tema_escolhido not in ['1', '2', '3', '4']:
            tema_escolhido = input(
                'Tema inválido. Escolha o tema pelo número correspondente: ')

        tema_escolhido = int(tema_escolhido)

        if tema_escolhido == 1:
            print('O tema escolhido foi Cidades')
            lista_cidades = temas['cidades']
            palavra = random.choice(lista_cidades)
        elif tema_escolhido == 2:
            print('O tema escolhido foi Objetos')
            lista_objetos = temas['objetos']
            palavra = random.choice(lista_objetos)
        elif tema_escolhido == 3:
            print('O tema escolhido foi Sobremesas')
            lista_sobremesas = temas['sobremesas']
            palavra = random.choice(lista_sobremesas)
        else:
            print('O tema escolhido foi Animais')
            lista_animais = temas['animais']
            palavra = random.choice(lista_animais)

    letras_erradas = []
    letras_acertadas = []
    vidas = 6

    while True:

        palavra_secreta = ''
        for letra in palavra:
            if letra in letras_acertadas:
                palavra_secreta += letra + ' '
            else:
                palavra_secreta += '_ '

        print(palavra_secreta)

        if letras_erradas:
            print('Letras erradas: ' + ' '.join(letras_erradas))

        letra = input('Digite uma letra: ').lower()

        if letra in letras_erradas or letra in letras_acertadas:
            print('Você já usou essa letra. Por favor, escolha outra letra.')
            continue

        if letra in palavra:
            letras_acertadas.append(letra)
            print('Muito bom! Você acertou essa letra!')
        else:
            letras_erradas.append(letra)
            print('Você errou! Essa letra não está na palavra secreta.')
            if len(letras_erradas) == 1:
                limpar_tela()
                print('  O  ')
            elif len(letras_erradas) == 2:
                limpar_tela()
                print('  O  ')
                print('  |  ')
            elif len(letras_erradas) == 3:
                limpar_tela()
                print('  O  ')
                print('  |  ')
                print('  |  ')
            elif len(letras_erradas) == 4:
                limpar_tela()
                print('  O  ')
                print(' \|/ ')
                print('  |  ')
            elif len(letras_erradas) == 5:
                limpar_tela()
                print('  O  ')
                print(' \|/ ')
                print('  |  ')
                print(' /   ')
            elif len(letras_erradas) == 6:
                limpar_tela()
                print('  O  ')
                print(' \|/ ')
                print('  |  ')
                print(' / \ ')
                print('/   \.')
                print(
                    f'Oh no! Sinto muito, você perdeu e foi enforcado! A palavra secreta era "{palavra}".')
                print('Não foi dessa vez, mas não desanime! Continue jogando ;)')
                break

        if all(letra in letras_acertadas for letra in palavra):
            print(f'Parabéns! Você acertou a palavra secreta: "{palavra}"!')
            print('Continue treinando suas habilidades! Vamos jogar novamente?')
            break

        if len(letras_erradas) == vidas:
            print(
                f'Ixi! Você atingiu o limite máximo de tentativas. A palavra era "{palavra}".')
            break

    return jogar_novamente()


while True:
    if not jogar_forca():
        break
