from playsound import playsound

musics = [
    '1', '2', '3', '4', '5'
]
play = input('Deseja repoduzir músicas? ')
if play == 's':
    print(f'Essas são as músicas disponíveis: \b{musics}')
    input('Qual música você deseja ouvir?')