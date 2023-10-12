from random import choice

lista = [
    'pedra',
    'papel',
    'tesoura'
]

bot_choice = [

];
best_of = 0;
best_of_1 = 0;
player_score = 0;
bot_score = 0;

print(
    'Bem vindo ao clássico jogo de Pedra, Papel e Tesoura!'
    )

start = input(
    'Vamos comecar? sim/não ' 
    )

if start == 'sim' or start == 's':
    best_of = int(input('Essa partida terá quantas rodadas? '))
    best_of_1 = best_of
    print(
        f'Excelente! Quem fizer mais pontos em {best_of} rodadas primeiro, vence. Vamos começar.'
        )
    
    while best_of != 0:
        bot_choice = choice(
            lista
            )
        escolha = input(
            'Escolha pedra, papel ou tesoura: '
            )
        
        if bot_choice == 'pedra':
            if escolha == 'pedra':
                print(
                    f'Empate! O bot também escolheu {bot_choice}.'
                )
            elif escolha == 'papel':
                player_score = player_score + 1
                best_of = best_of - 1
                print(
                    f'O bot escolheu {bot_choice} e você ganhou! Player {player_score} X {bot_score} Bot'
                ) 
                
            else:
                bot_score = bot_score + 1
                best_of = best_of - 1
                print(
                    f'O bot escolheu {bot_choice} e você perdeu! Player {player_score} X {bot_score} Bot'
                )
                
        elif bot_choice == 'papel':
            if escolha == 'papel':
                print(
                    f'Empate! O bot também escolheu {bot_choice}.'
                )
            elif escolha == 'tesoura':
                player_score = player_score + 1
                best_of = best_of - 1
                print(
                    f'O bot escolheu {bot_choice} e você ganhou! Player {player_score} X {bot_score} Bot'
                ) 
                
            else:
                bot_score = bot_score + 1
                best_of = best_of - 1
                print(
                    f'O bot escolheu {bot_choice} e você perdeu! Player {player_score} X {bot_score} Bot'
                )            

        else:
            if escolha == 'tesoura':
                print(
                    f'Empate! O bot também escolheu {bot_choice}.'
                )
            elif escolha == 'pedra':
                player_score = player_score + 1
                best_of = best_of - 1
                print(
                    f'O bot escolheu {bot_choice} e você ganhou! Player {player_score} X {bot_score} Bot'
                )    
                
            else:
                bot_score = bot_score + 1
                best_of = best_of - 1
                print(
                    f'O bot escolheu {bot_choice} e você perdeu! Player {player_score} X {bot_score} Bot'
                )

    else:
        if player_score >= bot_score:
            print(
                f'Parabéns! Você fez {player_score} pontos e o bot fez {bot_score} pontos nessas {best_of_1} rodadas e venceu o jogo!'
            )
            print(
            'Até a próxima!'
        )
        else:
            print(
                f'Que pena! O bot fez {bot_score} pontos e você fez {player_score} pontos nessas {best_of_1} rodadas e perdeu o jogo!'
            )
            print(
                'Até a próxima!'
            )
