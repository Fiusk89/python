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
		print(f'O número era {number}.')
		break
	else:
		guess = int(input(f'Escolha um número entre {low} e {high}. Você tem {trys} chances. '))
		if guess > high:
			print(f'O seu palpite não pode ser maior que {high}. Escolha outro número!')
		elif guess < low:
			print(f'O seu palpite não pode ser menor que {low}. Escolha outro número!')
		elif guess == number:
			print(f'Parabéns! Você acertou sobrando {trys} chances!')
		elif guess > number:
			high = print('Palpite muito alto!')
			high = guess
			trys = trys -1
		else:
			low = print('Palpite muito baixo!')
			low = guess
			trys = trys -1
print('FIM DE JOGO')
