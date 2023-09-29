#Escreva um programa que pergunte a quantidade de Km 
#percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, s
#abendo que o carro custava R$ 60,00 por dia e R$0,15 por Km rodado.

dia = 60
km_rodado = 0.15
days = int(input('Por quantos dias o carro foi alugado? '))
kms = int(input('Quantos Km foram rodados durante o aluguel? '))
print(f'Você alugou o carro por {days} dias e rodou {kms}Kms.\nSabendo que a diária custa R${dia:.2f} e é cobrado um adicional de R${km_rodado} por Km rodado:\nO seu total a pagar é R${dia * days + km_rodado * kms:.2f}.')
