from random import randint
numero = randint(0, 100)
palpite = 0
baixo = 0
alto = 100
chances = 5
while numero != palpite:
    p = int(input('Escolha um número entre {} e {}. Restam {} chances.'.format(baixo, alto, chances)))
    if palpite == numero:
        print('Parabéns! Você acertou sobrando {} chances!'.format(chances))
    elif palpite > numero:
        alto = print('Palpite muito alto!')
        alto = palpite
        chances = -1
    elif chances == 0:
        print('Que pena! Acabaram as suas chances!')
        break
    else:
        baixo = print('Palpite muito baixo!')
        baixo = palpite
        chances = -1