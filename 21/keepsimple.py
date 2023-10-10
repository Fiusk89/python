import random as rd

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
dealer = 0
player = 0
print(dealer)

dealer = rd.choice(deck)
print(dealer)
dealer = dealer + rd.choice(deck)
print(dealer)

while player < 21:
    if dealer <= 17:
        print('Dealer somou menos do que 17 pontos e vai pegar mais uma carta.')
        dealer = dealer + rd.choice(deck)
        print(dealer)
        if dealer > 21:
            print('O dealer "estourou" e você ganhou a rodada!')
            print(dealer)
            break
        else:    
            player = rd.choice(deck)
            print(player)
            player = player + rd.choice(deck)
            print(player)
            resposta = input(f'Sua vez! Você recebeu duas cartas, totalizando {player}, o deseja continuar? ')
            if resposta == 's':
                player = player + rd.choice(deck)
                print(player)
                resposta1 = input(f'Com mais uma carta, você totalizou {player}, vai continuar?')
                if resposta1 == 's':
                    player = player + rd.choice(deck)
                    print(player)            
                break