import random
from time import sleep

# configurações
valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
naipes = ['Ouros', 'Espadas', 'Paus', 'Copas']
face = ['Duque', '3', '4', '5', '6', '7', '8', '9']
face_10 = ['Valete', 'Dama', 'Rei']
fichas = 200
pontos_jogador = 0
pontos_cassino = 0
print('###VAMOS JOGAR 21!### \nO jogo será pelo terminal e você deverá responder com a letra S para SIM e N para NÃO. ')
# Jogo
start = input('Deseja começar? (s) (n) ')
if start == 's':
    while pontos_cassino < 21 or pontos_jogador < 21:
        pontos_cassino = random.choice(valor) * 2
        print('Crupier virou 2 cartas e somou', pontos_cassino, 'pontos.')
        pontos_jogador = random.choice(valor) * 2
        print('Você recebeu 2 cartas e somou', pontos_jogador, 'pontos.')
        if pontos_cassino < 17:
            print('O Crupier tem menos de 17 pontos e vai pegar mais uma carta.')
            pontos_cassino = pontos_cassino + random.choice(valor)
            print('Com a terceira carta, o crupier somou', pontos_cassino, 'pontos.')
            if pontos_cassino > 21:
                print('Ele ultrapassou os 21 pontos e você ganhou a rodada!'.format(pontos_cassino))
            input('Deseja pegar mais uma carta? ')
            if 's':
                pontos_jogador = pontos_jogador + random.choice(valor)
                print('Com a terceira carta, você somou', pontos_jogador, 'pontos.')           
        