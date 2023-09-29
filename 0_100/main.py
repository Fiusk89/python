from random import randint
number = randint(0, 100)
guess = 0
low = 0
high = 100
trys = 6
print('INÍCIO DE JOGO \nDIGITE O SEU PALPITE E BOA SORTE!')
while number != guess:
		if trys == 0:
			print('Que pena! Acabaram as suas chances!')
			break
		else:
			guess = int(input('Escolha um número entre {} e {}. Restam {} chances.'.format(low, high, trys)))
			if guess > high:
				print('O seu palpite não pode ser maior que {}. Escolha outro número!'.format(high))
			elif guess < low:
				print('O seu palpite não pode ser menor que {}. Escolha outro número!'.format(low))
			elif guess == number:
				print('Parabéns! Você acertou sobrando {} chances!'.format(trys))
			elif guess > number:
					high = print('Palpite muito alto!')
					high = guess
					trys = trys -1
			else:
						low = print('Palpite muito baixo!')
						low = guess
						trys = trys -1
print('FIM DE JOGO')
