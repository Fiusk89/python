from random import randint
number = randint(0, 100)
choice = 0
low = 0
high = 100
while choice != number:
	choice = int(input('Escolha um número entre {} e {}. Qual o seu palpite? '.format(low, high)))
	if choice == number:
		print('Parabéns, você acertou!')
	elif choice > number:
		print('Palpite muito alto!')
		high = choice
	else:
		print('Palpite muito baixo!')
		low = choice
