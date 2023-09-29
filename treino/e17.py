import math
print('Vamos calcular o comprimento da hipotenusa de um triângulo retângulo.')
cateto_oposto = int(input('Qual o comprimento do cateto oposto? '))
cateto_adjacente = int(input('Qual o comprimento do cateto adjacente? '))
print(f'O comprimento da hipotenusa de um triângulo retângulo com cateto oposto igual a {cateto_oposto} e cateto adjacente igual a {cateto_adjacente} é {math.hypot(cateto_adjacente, cateto_oposto)}')
    