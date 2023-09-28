from random import randint
number = randint(0, 100)
guess = 0
low = 0
high = 100
trys = 5
print('INÍCIO DE JOGO')
while number != guess:
    if trys == 0:
        print('Acabaram as suas chances. Você perdeu!')
        break
    guess = int(input('Escolha um número entre {} e {}. Restam {} chances.'.format(low, high, trys)))
    elif guess == number:
        print('Parabéns! Você acertou sobrando {} chances!'.format(trys))
    elif guess > number:
        high = print('Palpite muito alto!')
        high = guess
        trys = trys -1
    else:
        low = print('Palpite muito baixo!')
        low = guess
        trys = trys -1
print('FIM DE JOGO')